import unittest

from profile_similarity import symmetric_bma

PATIENT_TOY_PHENOTYPE_PROFILE = {"C", "B"}
GENE_TOY_PHENOTYPE_PROFILE = {"D", "A"}

EMPTY_PATIENT_PHENOTYPE_PROFILE = set()
EMPTY_GENE_PHENOTYPE_PROFILE = set()

IC_VALUES = {
    'ROOT': -0.0,
    'A': 0.5849625007211563,
    'C': 1.5849625007211563,
    'D': 1.5849625007211563,
    'B': 0.5849625007211563
    }

class TestSymmetricBMA(unittest.TestCase):
    def test_bma_normal_case(self):
        actual = symmetric_bma(
            PATIENT_TOY_PHENOTYPE_PROFILE,
            GENE_TOY_PHENOTYPE_PROFILE,
            IC_VALUES
            )
        expected = 0.5849625007211563
        self.assertAlmostEqual(actual, expected)

    def test_bma_with_both_profiles_empty(self):
        with self.assertRaises(ValueError):
            symmetric_bma(
                EMPTY_PATIENT_PHENOTYPE_PROFILE,
                EMPTY_GENE_PHENOTYPE_PROFILE,
                IC_VALUES
                )

    def test_bma_with_gene_profile_empty(self):
        with self.assertRaises(ValueError):
            symmetric_bma(
                PATIENT_TOY_PHENOTYPE_PROFILE,
                EMPTY_GENE_PHENOTYPE_PROFILE,
                IC_VALUES
                )