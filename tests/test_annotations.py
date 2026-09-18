import unittest

from annotations import annotation

TOY_GENE_ANNOTATIONS = {
    "g1": {"C"},
    "g2": {"D"},
    "g3": {"B"},
    "g_test": {"C", "D"}
}

TOY_PARENTS = {
    "ROOT": set(),
    "A": {"ROOT"},
    "B": {"ROOT"},
    "C": {"A"},
    "D": {"A", "B"}
}

class TestAnnotation(unittest.TestCase):
    def test_gene_with_one_HPO_term(self):
        actual = annotation(TOY_GENE_ANNOTATIONS, "g1")
        expected = {"C", "A", "ROOT"}
        self.assertEqual(actual, expected)

    def test_gene_with_multiple_HPO_terms(self):
        actual = annotation(TOY_GENE_ANNOTATIONS, "g_test")
        expected = {"C", "D", "A", "B", "ROOT"}
        self.assertEqual(actual, expected)