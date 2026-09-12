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
    N = len(propagated_annotations)
    information_content = {}
    for gene in propagated_annotations:
        for term in propagated_annotations[gene]:
            information_content[term] = information_content.get(term, 0) + 1/N
    for term in information_content:
        information_content[term] = -1*math.log2(information_content[term])
    return information_content