"""Provides MICA and Resnik semantic similarity calculations."""

from ontology import ancestors

def mica(term_1, term_2, ic_values):
    """Selects Most Informative Common Ancestor for two HPO terms.

    Args:
        term_1: HPO term.
        term_2: another HPO term.
        ic_values: Dictionary mapping each HPO term
        to its Information Content value.
    
    Raises:
        ValueError: If the two HPO terms have no common ancestor.
    
    Returns:
        The HPO term selected as the most informative common ancestor.
    """
    ancestors_1 = ancestors(term_1)
    ancestors_2 = ancestors(term_2)
    common_ancestors = ancestors_1.intersection(ancestors_2)
    if not common_ancestors:
        raise ValueError("No common ancestor found for the given HPO terms.")
    result = next(iter(common_ancestors))
    maximum = ic_values[result]
    for ancestor in common_ancestors:
        terms_ic = ic_values[ancestor]
        if terms_ic > maximum:
            maximum = terms_ic
            result = ancestor
    return result


def resnik(term_1, term_2, ic_values):
    """Returns Resnik semantic similarity measure for selected
    most informative common ancestor for two HPO terms.

    Args:
        term_1: HPO term.
        term_2: another HPO term.
        ic_values: Dictionary mapping each HPO term
        to its Information Content value.
    
    Returns:
        Information Content value of the HPO term
        selected by the MICA technique.
    """
    result = mica(term_1, term_2, ic_values)
    return ic_values[result]
