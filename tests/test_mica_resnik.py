import unittest

from semantic_similarity import select_mica, calculate_resnik
from ontology import Ontology

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

TEST_VALUEERROR_PARENTS = {
    "ROOT_X": set(),
    "A": {"ROOT_X"},
    "B": {"ROOT_X"},
    "C": {"A"},
    "D": {"A", "B"},
    "ROOT_Y": set(),
    "E": {"ROOT_Y"},
    "F": {"ROOT_Y"},
    "G": {"E", "F"}
}

class TestMICAandResnik(unittest.TestCase):
    def setUp(self):
        self.ontology = Ontology(TEST_PARENTS)

    def test_select_mica_with_shared_informative_ancestor(self):
        actual = select_mica("C", "D", IC_VALUES, self.ontology)
        expected = "A"
        self.assertEqual(actual, expected)

    def test_calculate_resnik_with_shared_informative_ancestor(self):
        actual = calculate_resnik("C", "D", IC_VALUES, self.ontology)
        expected = 0.5849625007211563
        self.assertAlmostEqual(actual, expected)

    def test_select_mica_with_root_as_only_common_ancestor(self):
        actual = select_mica("A", "B", IC_VALUES, self.ontology)
        expected = "ROOT"
        self.assertEqual(actual, expected)

    def test_calculate_resnik_with_root_as_mica(self):
        actual = calculate_resnik("A", "B", IC_VALUES, self.ontology)
        expected = -0.0
        self.assertAlmostEqual(actual, expected)

    def test_select_mica_for_identical_terms(self):
        actual = select_mica("B", "B", IC_VALUES, self.ontology)
        expected = "B"
        self.assertEqual(actual, expected)

    def test_calculate_resnik_for_identical_terms(self):
        actual = calculate_resnik("B", "B", IC_VALUES, self.ontology)
        expected = 0.5849625007211563
        self.assertAlmostEqual(actual, expected)

class TestMicaForValueError(unittest.TestCase):
    def setUp(self):
        self.ontology = Ontology(TEST_VALUEERROR_PARENTS)

    def test_select_mica_for_value_error(self):
        with self.assertRaisesRegex(
            ValueError,
            r"No common ancestor found for the given HPO terms\."
        ):
            select_mica("C", "G", {}, self.ontology)