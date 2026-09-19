import unittest

from semantic_similarity import mica, resnik
from ontology import Ontology

IC_VALUES = {
    'ROOT': -0.0,
    'A': 0.5849625007211563,
    'C': 1.5849625007211563,
    'D': 1.5849625007211563,
    'B': 0.5849625007211563
    }


TOY_PARENTS = {
    "ROOT": set(),
    "A": {"ROOT"},
    "B": {"ROOT"},
    "C": {"A"},
    "D": {"A", "B"}
}


class TestSemanticSimilarity(unittest.TestCase):
    def setUp(self):
            self.ontology = Ontology(TOY_PARENTS)

    def test_mica_with_shared_informative_ancestor(self):
        actual = mica("C", "D", IC_VALUES, self.ontology)
        expected = "A"
        self.assertEqual(actual, expected)

    def test_resnik_with_shared_informative_ancestor(self):
        actual = resnik("C", "D", IC_VALUES, self.ontology)
        expected = 0.5849625007211563
        self.assertAlmostEqual(actual, expected)

    def test_mica_with_root_as_only_common_ancestor(self):
        actual = mica("A", "B", IC_VALUES, self.ontology)
        expected = "ROOT"
        self.assertEqual(actual, expected)

    def test_resnik_with_root_as_mica(self):
        actual = resnik("A", "B", IC_VALUES, self.ontology)
        expected = -0.0
        self.assertAlmostEqual(actual, expected)

    def test_mica_for_identical_terms(self):
        actual = mica("B", "B", IC_VALUES, self.ontology)
        expected = "B"
        self.assertEqual(actual, expected)

    def test_resnik_for_identical_terms(self):
        actual = resnik("B", "B", IC_VALUES, self.ontology)
        expected = 0.5849625007211563
        self.assertAlmostEqual(actual, expected)