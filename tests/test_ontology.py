import unittest

from ontology import ancestors

TOY_PARENTS = {
    "ROOT": set(),
    "A": {"ROOT"},
    "B": {"ROOT"},
    "C": {"A"},
    "D": {"A", "B"}
}

class TestOntology(unittest.TestCase):
    def test_ancestors_result(self):
        actual = ancestors("D")
        expected = {"D", "A", "B", "ROOT"}
        self.assertEqual(actual, expected)

    def test_ancestors_root(self):
        actual = ancestors("ROOT")
        expected = {"ROOT"}
        self.assertEqual(actual, expected)