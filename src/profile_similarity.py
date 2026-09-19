"""Provides phenotype profile similarity measures."""

from semantic_similarity import resnik

def symmetric_bma(patient_phenotype_profile, gene_phenotype_profile, ic_values):
    """Computes pairwise Resnik similarities between patient and gene phenotype terms,
    selects the best matches in both directions,
    and computes the symmetric Best Match Average.

    Args:
        patient_phenotype_profile: Patient's human ontology phenotype profile.
        gene_phenotype_profile: Gene's annotated human ontology phenotype profile.
        ic_values: Dictionary mapping each HPO term to its Information Content value.

    Returns:
        Symmetric Best Match Average score between the patient and gene phenotype profiles.
    """
    if not patient_phenotype_profile or not gene_phenotype_profile:
        raise ValueError("Patient or gene phenotype profile must not be empty.")
    patient_side_best_matches = []
    for patient_term in patient_phenotype_profile:
        maximum = 0
        for gene_term in gene_phenotype_profile:
            resnik_value = resnik(patient_term, gene_term, ic_values)
            maximum = max(maximum, resnik_value)
        patient_side_best_matches.append(maximum)
    average_patient_side_best_matches = sum(
        patient_side_best_matches)/len(patient_side_best_matches)

    gene_side_best_matches = []
    for gene_term in gene_phenotype_profile:
        maximum = 0
        for patient_term in patient_phenotype_profile:
            resnik_value = resnik(gene_term, patient_term, ic_values)
            maximum = max(maximum, resnik_value)
        gene_side_best_matches.append(maximum)
    average_gene_side_best_matches = sum(
        gene_side_best_matches)/len(gene_side_best_matches)

    directional_averages = (
        average_patient_side_best_matches + average_gene_side_best_matches)/2
    return directional_averages


def jaccard(patient_phenotype_profile, gene_phenotype_profile):
    """Computes the Jaccard similarity between two non-empty phenotype profiles
    based on exact HPO term overlap.

    Args:
        patient_phenotype_profile: Patient's human ontology phenotype profile.
        gene_phennotype_profile: Gene's annotated human ontology phenotype profile.

    Returns:
        Jaccard value.
    """
    if not patient_phenotype_profile or not gene_phenotype_profile:
        raise ValueError("Patient or gene phenotype profile must not be empty.")
    intersection_terms = patient_phenotype_profile.intersection(gene_phenotype_profile)
    union_terms = patient_phenotype_profile.union(gene_phenotype_profile)
    jaccard_result = len(intersection_terms)/len(union_terms)
    return jaccard_result
