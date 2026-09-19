import unittest

from ontology import Ontology

TOY_PARENTS = {
    "ROOT": set(),
    "A": {"ROOT"},
    "B": {"ROOT"},
    "C": {"A"},
    "D": {"A", "B"}
}

class TestOntology(unittest.TestCase):
    def setUp(self):
        self.ontology = Ontology(TOY_PARENTS)

    def test_ancestors_result(self):
        actual = self.ontology.ancestors("D")
        expected = {"D", "A", "B", "ROOT"}
        self.assertEqual(actual, expected)

    def test_ancestors_root(self):
        actual = self.ontology.ancestors("ROOT")
        expected = {"ROOT"}
        self.assertEqual(actual, expected)