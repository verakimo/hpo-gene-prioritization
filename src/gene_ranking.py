"""Provides phenotype-based gene scoring, ranking, and output formatting."""

from profile_similarity import symmetric_bma

def score_genes(patient_phenotype_profile, gene_phenotype_profiles, ic_values):
    """Computes symmetric BMA for patient phenotype profile and genes in gene phenotype profiles.

    Args:
        patient_phenotype_profile: Set of HPO terms describing the patient's phenotype.
        gene_phenotype_profiles: Dictionary mapping each gene to its set of annotated HPO terms.
        ic_values: Dictionary mapping each HPO term to its Information Content value.

    Returns:
        Dictionary mapping each gene to its symmetric BMA score.
    """
    gene_scores = {}
    for gene in gene_phenotype_profiles:
        gene_scores[gene] = symmetric_bma(
            patient_phenotype_profile,
            gene_phenotype_profiles[gene],
            ic_values
            )
    return gene_scores


def rank_genes(gene_scores):
    """Ranks genes by BMA score in descending order.

    Args:
        gene_scores: BMA scores for genes.
    
    Returns:
        Dictionary mapping genes to BMA scores in descending score order.
    """
    ranked_genes = dict(
        sorted(
            gene_scores.items(),
            key=lambda item: item[1],
            reverse=True
            )
        )
    return ranked_genes


def rich_output(ranked_genes, gene_phenotype_profiles):
    """Creates a ranked output containing each gene's rank,
    BMA score, and phenotype annotations.

    Args:
        ranked_genes: Sorted dictionary mapping each gene to its BMA score.
        gene_phenotype_profiles: Dictionary mapping each gene to its set of annotated HPO terms.
    
    Returns:
        List of dictionaries containing rank, gene, score, and phenotype annotations.
    """
    top_rank = []
    n = 1
    for gene in ranked_genes:
        richer_output = {
            "rank": n,
            "gene": gene,
            "score": ranked_genes[gene],
            "phenotypes": gene_phenotype_profiles[gene]
        }
        top_rank.append(richer_output)
        n += 1
    return top_rank
