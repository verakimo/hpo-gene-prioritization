import unittest

from annotations import propagation
from ontology import Ontology

TEST_GENE_ANNOTATIONS = {
    "g1": {"C"},
    "g2": {"D"},
    "g3": {"B"},
    "g_test": {"C", "D"}
}

EMPTY_DATASET = {}

TOY_PARENTS = {
    "ROOT": set(),
    "A": {"ROOT"},
    "B": {"ROOT"},
    "C": {"A"},
    "D": {"A", "B"}
}


class TestPropagation(unittest.TestCase):
    def setUp(self):
        self.ontology = Ontology(TOY_PARENTS)

    def test_general_dataset(self):
        actual = propagation(TEST_GENE_ANNOTATIONS, self.ontology)
        expected = {
            "g1": {"C", "A", "ROOT"},
            "g2": {"D", "A", "B", "ROOT"},
            "g3": {"B", "ROOT"},
            "g_test": {"A", "B", "C", "D", "ROOT"}
        }
        self.assertEqual(actual, expected)

    def test_empty_dataset(self):
        actual = propagation(EMPTY_DATASET, self.ontology)
        expected = {}
        self.assertEqual(actual, expected)