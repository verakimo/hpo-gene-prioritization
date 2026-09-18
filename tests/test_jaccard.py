import unittest

from profile_similarity import jaccard

PATIENT_TOY_PHENOTYPE_PROFILE_1 = {"C", "B"}
GENE_TOY_PHENOTYPE_PROFILE_1 = {"D", "A"}

PATIENT_TOY_PHENOTYPE_PROFILE_2 = {"C", "B"}
GENE_TOY_PHENOTYPE_PROFILE_2 = {"B", "D"}

EMPTY_PATIENT_PHENOTYPE_PROFILE = set()
EMPTY_GENE_PHENOTYPE_PROFILE = set()



class TestJaccard(unittest.TestCase):
    def test_jaccard_no_overlap(self):
        actual = jaccard(
            PATIENT_TOY_PHENOTYPE_PROFILE_1,
            GENE_TOY_PHENOTYPE_PROFILE_1
            )
        expected = 0
        self.assertEqual(actual, expected)

    def test_jaccard_partial_overlap(self):
        actual = jaccard(
            PATIENT_TOY_PHENOTYPE_PROFILE_2,
            GENE_TOY_PHENOTYPE_PROFILE_2
            )
        expected = 1/3
        self.assertAlmostEqual(actual, expected)

    def test_jaccard_with_both_profiles_empty(self):
        with self.assertRaises(ValueError):
            jaccard(
                EMPTY_PATIENT_PHENOTYPE_PROFILE,
                EMPTY_GENE_PHENOTYPE_PROFILE
                )

    def test_jaccard_with_gene_profile_empty(self):
        with self.assertRaises(ValueError):
            jaccard(
                PATIENT_TOY_PHENOTYPE_PROFILE_1,
                EMPTY_GENE_PHENOTYPE_PROFILE
                )