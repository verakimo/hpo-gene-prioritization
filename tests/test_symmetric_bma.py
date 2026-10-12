import unittest

from semantic_similarity import calculate_symmetric_bma
from ontology import Ontology

PATIENT_TEST_PHENOTYPE_PROFILE = {"C", "B"}
GENE_TEST_PHENOTYPE_PROFILE = {"D", "A"}

EMPTY_PATIENT_PHENOTYPE_PROFILE = set()
EMPTY_GENE_PHENOTYPE_PROFILE = set()

IC_VALUES = {
    "ROOT": -0.0,
    "A": 0.5849625007211563,
    "C": 1.5849625007211563,
    "D": 1.5849625007211563,
    "B": 0.5849625007211563
}

TEST_PARENTS = {
    "ROOT": set(),
    "A": {"ROOT"},
    "B": {"ROOT"},
    "C": {"A"},
    "D": {"A", "B"}
}

class TestSymmetricBMA(unittest.TestCase):
    def setUp(self):
        self.ontology = Ontology(TEST_PARENTS)

    def test_bma_normal_case(self):
        actual = calculate_symmetric_bma(
            PATIENT_TEST_PHENOTYPE_PROFILE,
            GENE_TEST_PHENOTYPE_PROFILE,
            IC_VALUES,
            self.ontology
            )
        expected = 0.5849625007211563
        self.assertAlmostEqual(actual, expected)

    def test_bma_with_both_profiles_empty(self):
        with self.assertRaises(ValueError):
            calculate_symmetric_bma(
                EMPTY_PATIENT_PHENOTYPE_PROFILE,
                EMPTY_GENE_PHENOTYPE_PROFILE,
                IC_VALUES,
                self.ontology
                )

    def test_bma_with_gene_profile_empty(self):
        with self.assertRaises(ValueError):
            calculate_symmetric_bma(
                PATIENT_TEST_PHENOTYPE_PROFILE,
                EMPTY_GENE_PHENOTYPE_PROFILE,
                IC_VALUES,
                self.ontology
                )