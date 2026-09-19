"""Provides Information Content calculation for HPO terms."""

import math

def information_content(propagated_annotations):
    """Computes Information Content for HPO terms
    from propagated gene annotations.

    Args:
        propagated_annotations: Dictionary mapping each gene to 
        its propagated HPO terms.

    Returns:
        Dictionary mapping each HPO term to its Information Content value.
    """
    total_genes = len(propagated_annotations)
    ic_values = {}
    for gene in propagated_annotations:
        for term in propagated_annotations[gene]:
            ic_values[term] = ic_values.get(term, 0) + 1/total_genes
    for term in ic_values:
        ic_values[term] = -1*math.log2(ic_values[term])
    return ic_values
