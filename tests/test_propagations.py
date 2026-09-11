import unittest

from annotations import propagation

test_gene_annotations = {
    "g1": {"C"},
    "g2": {"D"},
    "g3": {"B"},
    "g_test": {"C", "D"}
}

empty_dataset = {}

class TestPropagation(unittest.TestCase):
    def test_general_dataset(self):
        actual = propagation(test_gene_annotations)
        expected = {
            "g1": {"C", "A", "ROOT"},
            "g2": {"D", "A", "B", "ROOT"},
            "g3": {"B", "ROOT"},
            "g_test": {"A", "B", "C", "D", "ROOT"}
        }
        self.assertEqual(actual, expected)

    def test_empty_dataset(self):
        actual = propagation(empty_dataset)
        expected = {}
        self.assertEqual(actual, expected)