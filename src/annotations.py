from ontology import ancestors

toy_gene_annotations = {
    "g1": {"C"},
    "g2": {"D"},
    "g3": {"B"}
}

def annotation(gene):
    """Propagates the direct HPO annotations of a given gene.
    For each HPO term, finds the ancestor-or-self set.
    Combines these sets.

    Args:
        gene: Identifier of the gene whose annotations are propagated.
    
    Returns:
        The union of the ancestor-or-self sets of gene's HPO annotations.
    """
    terms = toy_gene_annotations[gene]
    terms_ancestors = set()
    for term in terms:
        terms_ancestors.update(ancestors(term))
    return terms_ancestors