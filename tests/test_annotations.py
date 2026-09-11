import unittest

from annotations import annotation

test_gene_annotations = {
    "g1": {"C"},
    "g2": {"D"},
    "g3": {"B"},
    "g_test": {"C", "D"}
}

class TestAnnotation(unittest.TestCase):
    def test_gene_with_one_HPO_term(self):
        actual = annotation(test_gene_annotations, "g1")
        expected = {"C", "A", "ROOT"}
        self.assertEqual(actual, expected)

    def test_gene_with_multiple_HPO_terms(self):
        actual = annotation(test_gene_annotations, "g_test")
        expected = {"C", "D", "A", "B", "ROOT"}
        self.assertEqual(actual, expected)