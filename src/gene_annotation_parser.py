"""Provides functions for parsing gene-to-phenotype annotation data."""

def parse_gene_annotations(file_path):
    """Parse gene-to-phenotype annotations from a tab-separated text file.

    Args:
        file_path: Path to the gene-to-phenotype annotation file.

    Returns:
        A dictionary mapping each gene symbol to a set of direct HPO terms.
    """
    genes_annotations = {}
    with open(file_path, encoding="utf-8") as genes_to_phenotype:
        next(genes_to_phenotype)
        for line in genes_to_phenotype:
            parts = line.split("\t")
            gene = parts[1]
            hpo_term = parts[2]
            if gene not in genes_annotations:
                genes_annotations[gene] = set()
            genes_annotations[gene].add(hpo_term)
    return genes_annotations
