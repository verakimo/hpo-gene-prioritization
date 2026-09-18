import unittest

from annotations import propagation

TEST_GENE_ANNOTATIONS = {
    "g1": {"C"},
    "g2": {"D"},
    "g3": {"B"},
    "g_test": {"C", "D"}
}

EMPTY_DATASET = {}

class TestPropagation(unittest.TestCase):
    def test_general_dataset(self):
        actual = propagation(TEST_GENE_ANNOTATIONS)
        expected = {
            "g1": {"C", "A", "ROOT"},
            "g2": {"D", "A", "B", "ROOT"},
            "g3": {"B", "ROOT"},
            "g_test": {"A", "B", "C", "D", "ROOT"}
        }
        self.assertEqual(actual, expected)

    def test_empty_dataset(self):
        actual = propagation(EMPTY_DATASET)
        expected = {}
        self.assertEqual(actual, expected)