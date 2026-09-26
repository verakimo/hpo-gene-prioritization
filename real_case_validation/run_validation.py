"""Validates HPO-based gene prioritization using real solved Phenopacket cases.

Reads patient phenotype profiles and known causal genes from Phenopacket JSON
files, ranks genes using the phenotype-driven prioritization pipeline, and
reports the rank of the known causal gene for each processed patient case.
"""

import json
import os
import time

from annotations import propagation
from gene_annotation_parser import parse_gene_annotations
from gene_ranking import rank_genes, rich_output, score_genes
from hpo_parser import parse_obo
from information_content import information_content
from ontology import Ontology

HPO_FILE = "data/hp.obo"
GENE_ANNOTATION_FILE = "data/genes_to_phenotype.txt"
TOP_RESULTS = 10

FILE_PATH = "real_case_validation/benchmark_data/0.1.27"

VALIDATION_COHORTS = (
    "ABCA4",
    "F8",
    "GALT",
    "OCA2"
)


def is_solved(patient_data):
    """Check whether a Phenopacket contains a solved interpretation.

    Args:
        patient_data: Parsed Phenopacket JSON data.

    Returns:
        True if the case contains a solved interpretation, otherwise False.
    """
    for interpretation in patient_data.get("interpretations", []):
        if interpretation.get("progressStatus") == "SOLVED":
            return True
    return False


def fetch_phenotypic_features(patient_data):
    """Extract present HPO phenotype terms from a Phenopacket.

    Args:
        patient_data: Parsed Phenopacket JSON data.

    Returns:
        A set of HPO IDs for phenotypic features that are not excluded.
    """
    patient_phenotypic_features = set()

    for phenotypic_feature in patient_data["phenotypicFeatures"]:
        if not phenotypic_feature.get("excluded", False):
            patient_phenotypic_features.add(phenotypic_feature["type"]["id"])

    return patient_phenotypic_features


def fetch_causal_gene(patient_data):
    """Extract the causal gene symbol from a solved Phenopacket.

    Args:
        patient_data: Parsed Phenopacket JSON data.

    Returns:
        The causal gene symbol, or None if it cannot be determined.
    """
    for interpretation in patient_data.get("interpretations", []):
        if interpretation.get("progressStatus") != "SOLVED":
            continue

        genomic_interpretations = interpretation["diagnosis"]["genomicInterpretations"]

        for genomic_interpretation in genomic_interpretations:
            if genomic_interpretation.get("interpretationStatus") == "CAUSATIVE":
                return genomic_interpretation[
                    "variantInterpretation"]["variationDescriptor"]["geneContext"]["symbol"]

    return None


def run_hpo_gene_prioritization(
    ontology,
    gene_annotations,
    ic_values,
    patient,
    patient_profile,
    validation_gene
):
    """Rank genes for one patient and record the known causal gene rank.

    Args:
        ontology: HPO ontology used for semantic similarity calculations.
        gene_annotations: Direct gene-to-phenotype annotations.
        ic_values: Information Content values for propagated HPO terms.
        patient: Name of the patient Phenopacket file.
        patient_profile: Set of the patient's present HPO terms.
        validation_gene: Known causal gene used for validation.

    Returns:
        A dictionary containing the patient, causal gene, phenotype count,
        causal gene rank, and whether the gene is ranked in the top 10.
    """
    gene_scores = score_genes(
        patient_profile,
        gene_annotations,
        ic_values,
        ontology
    )
    ranked_genes = rank_genes(gene_scores)
    output = rich_output(
        ranked_genes,
        gene_annotations
    )

    one_patient_validation_result = {
        "Patient": patient,
        "Gene": validation_gene,
        "Gene in top 10 results": "No",
        "Rank": "Not found",
        "Number of patient HPO terms": len(patient_profile)
    }

    for result in output:
        if result["gene"] == validation_gene:
            one_patient_validation_result["Rank"] = result["rank"]

            if result["rank"] <= TOP_RESULTS:
                one_patient_validation_result["Gene in top 10 results"] = "Yes"

            break

    return one_patient_validation_result


def create_validation_inputs(file_path, cohort):
    """Create validation inputs from one Phenopacket cohort folder.

    Args:
        file_path: Path to the extracted Phenopacket Store release.
        cohort: Name of the cohort folder to process.

    Returns:
        A list of patient validation inputs extracted from solved Phenopackets.
    """
    cohort_path = os.path.join(file_path, cohort)

    if not os.path.isdir(cohort_path):
        print(f"{cohort}: Skipped: cohort directory was not found")
        return []

    validation_inputs = []

    for patient in sorted(os.listdir(cohort_path)):
        if not patient.endswith(".json"):
            continue

        patient_path = os.path.join(cohort_path, patient)

        with open(patient_path, encoding="utf-8") as file_data:
            patient_data = json.load(file_data)

        if not is_solved(patient_data):
            print(f"{patient}: Skipped: case is not solved")
            continue

        validation_gene = fetch_causal_gene(patient_data)

        if validation_gene is None:
            print(f"{patient}: Skipped: causal gene could not be determined")
            continue

        patient_phenotypic_features = fetch_phenotypic_features(patient_data)

        validation_inputs.append((patient, patient_phenotypic_features, validation_gene))

    return validation_inputs


def print_output(validation_results, program_time):
    """Print grouped validation results and runtime statistics."""
    if not validation_results:
        print("\nNo validation cases were processed.\n")
        return

    result_matrix = []
    causal_gene = ""

    empty_output = {
        "causal_gene": "",
        "top_10": 0,
        "ranked_1": 0,
        "cases": 0,
        "top_10_percentage": 0,
        "ranked_1_percentage": 0
    }

    result_dictionary_for_causal_gene = empty_output.copy()

    in_top = 0
    in_rank_1 = 0

    for result in validation_results:
        if causal_gene == "":
            causal_gene = result["Gene"]
            result_dictionary_for_causal_gene["causal_gene"] = causal_gene

        elif causal_gene != result["Gene"]:
            result_dictionary_for_causal_gene["top_10_percentage"] = (
                100
                * result_dictionary_for_causal_gene["top_10"]
                / result_dictionary_for_causal_gene["cases"]
            )
            result_dictionary_for_causal_gene["ranked_1_percentage"] = (
                100
                * result_dictionary_for_causal_gene["ranked_1"]
                / result_dictionary_for_causal_gene["cases"]
            )
            result_matrix.append(result_dictionary_for_causal_gene)
            causal_gene = result["Gene"]
            result_dictionary_for_causal_gene = empty_output.copy()
            result_dictionary_for_causal_gene["causal_gene"] = causal_gene

        if result["Gene in top 10 results"] == "Yes":
            result_dictionary_for_causal_gene["top_10"] += 1
            in_top += 1

        if result["Rank"] == 1:
            result_dictionary_for_causal_gene["ranked_1"] += 1
            in_rank_1 += 1

        result_dictionary_for_causal_gene["cases"] += 1

    # Add the last causal gene to the result matrix.
    result_dictionary_for_causal_gene["top_10_percentage"] = (
        100
        * result_dictionary_for_causal_gene["top_10"]
        / result_dictionary_for_causal_gene["cases"]
    )
    result_dictionary_for_causal_gene["ranked_1_percentage"] = (
        100
        * result_dictionary_for_causal_gene["ranked_1"]
        / result_dictionary_for_causal_gene["cases"]
    )
    result_matrix.append(result_dictionary_for_causal_gene)

    total_cases = len(validation_results)
    total_top_10_percentage = 100 * in_top/total_cases
    total_ranked_1_percentage = 100 * in_rank_1/total_cases

    print(
        "\nThe results of the empirical validation "
        "on the benchmark data are as follows:\n"
    )

    print(
        f"Cases with the causal gene in the top 10: "
        f"{in_top}/{total_cases}"
    )

    print(
        f"Cases with the causal gene ranked #1: "
        f"{in_rank_1}/{total_cases}\n"
    )

    print(
        f"{'Causal gene':<14}"
        f"{'Cases':>8}"
        f"{'Ranked #1':>12}"
        f"{'Ranked #1 (%)':>16}"
        f"{'Top 10':>10}"
        f"{'Top 10 (%)':>14}"
    )

    print("-" * 74)

    for gene in result_matrix:
        print(
            f"{gene['causal_gene']:<14}"
            f"{gene['cases']:>8}"
            f"{gene['ranked_1']:>12}"
            f"{gene['ranked_1_percentage']:>15.2f}%"
            f"{gene['top_10']:>10}"
            f"{gene['top_10_percentage']:>13.2f}%"
        )

    print("-" * 74)

    print(
        f"{'TOTAL':<14}"
        f"{total_cases:>8}"
        f"{in_rank_1:>12}"
        f"{total_ranked_1_percentage:>15.2f}%"
        f"{in_top:>10}"
        f"{total_top_10_percentage:>13.2f}%"
    )

    average_time = program_time / total_cases

    print()
    print(f"Processed cases: {total_cases}")
    print(f"Validation runtime: {program_time:.2f} seconds")
    print(f"Average time per case: {average_time:.2f} seconds")
    print()


def run_validation():
    """Run empirical validation on selected Phenopacket Store cohorts.

    Loads the HPO ontology and gene annotations, processes solved patient
    Phenopackets from selected cohorts, ranks candidate genes, and sends
    the collected results to the output function.
    """
    start_time = time.perf_counter()

    validation_results = []

    parents = parse_obo(HPO_FILE)
    ontology = Ontology(parents)
    gene_annotations = parse_gene_annotations(GENE_ANNOTATION_FILE)
    propagated_annotations = propagation(gene_annotations, ontology)
    ic_values = information_content(propagated_annotations)

    for cohort in VALIDATION_COHORTS:
        validation_inputs = create_validation_inputs(FILE_PATH, cohort)

        for patient, patient_profile, validation_gene in validation_inputs:
            one_patient_validation_result = (
                run_hpo_gene_prioritization(
                    ontology,
                    gene_annotations,
                    ic_values,
                    patient,
                    patient_profile,
                    validation_gene
                )
            )

            validation_results.append(one_patient_validation_result)

    end_time = time.perf_counter()
    program_time = end_time - start_time

    print_output(validation_results, program_time)


if __name__ == "__main__":
    run_validation()
