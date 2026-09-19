from annotations import propagation
from gene_annotation_parser import parse_gene_annotations
from gene_ranking import rank_genes, rich_output, score_genes
from hpo_parser import parse_obo
from information_content import information_content
from ontology import Ontology


HPO_FILE = "data/hp.obo"
GENE_ANNOTATION_FILE = "data/genes_to_phenotype.txt"
TOP_RESULTS = 10


def main():
    parents = parse_obo(HPO_FILE)
    ontology = Ontology(parents)
    gene_annotations = parse_gene_annotations(GENE_ANNOTATION_FILE)

    propagated_annotations = propagation(gene_annotations, ontology)
    ic_values = information_content(propagated_annotations)

    user_input = input(
    "Enter the patient's phenotype terms as Human Phenotype Ontology (HPO) IDs separated by spaces (e.g. HP:0002460 HP:0002451): ")
    patient_profile = set(user_input.split())

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

    print("\nTop gene candidates:\n")
    for result in output[:TOP_RESULTS]:
        phenotypes = sorted(result["phenotypes"])
        matching_phenotypes = patient_profile.intersection(result["phenotypes"])

        print(f"{result['rank']}. {result['gene']}")
        print(f"Score: {result['score']:.4f}")
        print(f"Direct phenotypes: {len(phenotypes)}")
        print(f"Input phenotype matches: {len(matching_phenotypes)}/{len(patient_profile)}")
        if matching_phenotypes:
            print("Matching HPO terms: " + ", ".join(sorted(matching_phenotypes)))
        else:
            print("Matching HPO terms: none")
        print("First HPO terms: " + ", ".join(phenotypes[:10]))
        print()


if __name__ == "__main__":
    main()
