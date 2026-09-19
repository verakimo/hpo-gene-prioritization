"""Provides functions for propagating gene phenotype annotations."""

def annotation(data, gene, ontology):
    """Propagates the direct HPO annotations of a given gene.
    For each HPO term, finds the ancestor-or-self set.
    Combines these sets.

    Args:
        data: Mapping from gene identifiers to sets of direct HPO terms.
        gene: Identifier of the gene whose annotations are propagated.
        ontology: An Ontology object used to retrieve ancestors of HPO terms.
    
    Returns:
        The union of the ancestor-or-self sets of gene's HPO annotations.
    """
    terms = data[gene]
    terms_ancestors = set()
    for term in terms:
        terms_ancestors.update(ontology.ancestors(term))
    return terms_ancestors


def propagation(data, ontology):
    """Propagates direct HPO annotations for all genes in the dataset.

    Args:
        data: Mapping from gene identifiers to sets of direct HPO terms.
        ontology: An Ontology object used to retrieve ancestors of HPO terms.
    
    Returns:
        Dictionary mapping each gene to its propagated HPO terms.
    """
    propagated_annotations = {}
    for gene in data:
        propagated_annotations[gene] = annotation(data, gene, ontology)
    return propagated_annotations
