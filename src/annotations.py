from ontology import ancestors

toy_gene_annotations = {
    "g1": {"C"},
    "g2": {"D"},
    "g3": {"B"}
}

def annotation(data, gene):
    """Propagates the direct HPO annotations of a given gene.
    For each HPO term, finds the ancestor-or-self set.
    Combines these sets.

    Args:
        data: Mapping from gene identifiers to sets of direct HPO terms.
        gene: Identifier of the gene whose annotations are propagated.
    
    Returns:
        The union of the ancestor-or-self sets of gene's HPO annotations.
    """
    terms = data[gene]
    terms_ancestors = set()
    for term in terms:
        terms_ancestors.update(ancestors(term))
    return terms_ancestors


def propagation(data):
    """Propagates direct HPO annotations for all genes in the dataset.

    Args:
        data: Mapping from gene identifiers to sets of direct HPO terms.
    
    Returns:
        Dictionary mapping each gene to its propagated HPO terms.
    """
    propagated_annotations = {}
    for gene in data:
        propagated_annotations[gene] = annotation(data, gene)
    return propagated_annotations