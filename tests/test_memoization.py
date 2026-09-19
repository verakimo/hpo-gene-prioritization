import unittest

from ontology import Ontology

TOY_PARENTS = {
    "ROOT": set(),
    "A": {"ROOT"},
    "B": {"ROOT"},
    "C": {"A"},
    "D": {"A", "B"}
}

class TestMemoization(unittest.TestCase):
    def setUp(self):
        self.ontology = Ontology(TOY_PARENTS)

    def test_ancestor_cache(self):
        self.ontology.ancestor_cache.clear()
        self.assertNotIn("D", self.ontology.ancestor_cache)
        self.ontology.ancestors("D")
        self.assertIn("D", self.ontology.ancestor_cache)
        actual = self.ontology.ancestor_cache["D"]
        expected = {"D", "A", "B", "ROOT"}
        self.assertEqual(actual, expected)
