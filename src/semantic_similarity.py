"""Calculates semantic similarity between HPO terms and phenotype profiles.

This module implements MICA selection and the Resnik similarity measure for pairs
of HPO terms, and symmetric Best Match Average (BMA) for comparing phenotype profiles.
"""

def select_mica(term_1, term_2, ic_values, ontology):
    """Selects Most Informative Common Ancestor for two HPO terms.

    Args:
        term_1: HPO term.
        term_2: another HPO term.
        ic_values: Dictionary mapping each HPO term
        to its Information Content value.
        ontology: An Ontology object used to retrieve ancestors of HPO terms.
    
    Raises:
        ValueError: If the two HPO terms have no common ancestor.
    
    Returns:
        The HPO term selected as the most informative common ancestor.
    """
    ancestors_1 = ontology.get_ancestors(term_1)
    ancestors_2 = ontology.get_ancestors(term_2)
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


def calculate_resnik(term_1, term_2, ic_values, ontology):
    """Calculates Resnik semantic similarity measure for selected
    Most Informative Common Ancestor for two HPO terms.

    Args:
        term_1: HPO term.
        term_2: another HPO term.
        ic_values: Dictionary mapping each HPO term
        to its Information Content value.
        ontology: An Ontology object used to retrieve ancestors of HPO terms.
    
    Returns:
        Information Content value of the HPO term
        selected by the MICA technique.
    """
    result = select_mica(term_1, term_2, ic_values, ontology)
    return ic_values[result]


def calculate_symmetric_bma(patient_phenotype_profile, gene_phenotype_profile, ic_values, ontology):
    """Calculates pairwise Resnik similarities between patient and gene phenotype terms,
    selects the best matches in both directions,
    and calculates the symmetric Best Match Average.

    Args:
        patient_phenotype_profile: Patient's human ontology phenotype profile.
        gene_phenotype_profile: Gene's annotated human ontology phenotype profile.
        ic_values: Dictionary mapping each HPO term to its Information Content value.
        ontology: An Ontology object used to retrieve ancestors of HPO terms.

    Returns:
        Symmetric Best Match Average score between the patient and gene phenotype profiles.
    """
    if not patient_phenotype_profile or not gene_phenotype_profile:
        raise ValueError("Patient or gene phenotype profile must not be empty.")
    patient_side_best_matches = []
    for patient_term in patient_phenotype_profile:
        maximum = 0
        for gene_term in gene_phenotype_profile:
            resnik_value = calculate_resnik(patient_term, gene_term, ic_values, ontology)
            maximum = max(maximum, resnik_value)
        patient_side_best_matches.append(maximum)
    average_patient_side_best_matches = sum(
        patient_side_best_matches)/len(patient_side_best_matches)

    gene_side_best_matches = []
    for gene_term in gene_phenotype_profile:
        maximum = 0
        for patient_term in patient_phenotype_profile:
            resnik_value = calculate_resnik(gene_term, patient_term, ic_values, ontology)
            maximum = max(maximum, resnik_value)
        gene_side_best_matches.append(maximum)
    average_gene_side_best_matches = sum(
        gene_side_best_matches)/len(gene_side_best_matches)

    directional_averages = (
        average_patient_side_best_matches + average_gene_side_best_matches)/2
    return directional_averages
