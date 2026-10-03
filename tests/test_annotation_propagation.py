import unittest

from annotation_propagation import propagate_gene_annotations, propagate_all_annotations
from ontology import Ontology

TOY_GENE_ANNOTATIONS = {
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

class TestPropagateGeneAnnotations(unittest.TestCase):
    def setUp(self):
        self.ontology = Ontology(TOY_PARENTS)
    def test_gene_with_one_HPO_term(self):
        actual = propagate_gene_annotations(TOY_GENE_ANNOTATIONS, "g1", self.ontology)
        expected = {"C", "A", "ROOT"}
        self.assertEqual(actual, expected)

    def test_gene_with_multiple_HPO_terms(self):
        actual = propagate_gene_annotations(TOY_GENE_ANNOTATIONS, "g_test", self.ontology)
        expected = {"C", "D", "A", "B", "ROOT"}
        self.assertEqual(actual, expected)


class TestPropagateAllAnnotations(unittest.TestCase):
    def setUp(self):
        self.ontology = Ontology(TOY_PARENTS)

    def test_general_dataset(self):
        actual = propagate_all_annotations(TOY_GENE_ANNOTATIONS, self.ontology)
        expected = {
            "g1": {"C", "A", "ROOT"},
            "g2": {"D", "A", "B", "ROOT"},
            "g3": {"B", "ROOT"},
            "g_test": {"A", "B", "C", "D", "ROOT"}
        }
        self.assertEqual(actual, expected)

    def test_empty_dataset(self):
        actual = propagate_all_annotations(EMPTY_DATASET, self.ontology)
        expected = {}
        self.assertEqual(actual, expected)