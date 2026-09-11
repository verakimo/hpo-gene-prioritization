import unittest

from ontology import ancestors

class TestOntology(unittest.TestCase):
    def test_ancestors_result(self):
        actual = ancestors("D")
        expected = {"D", "A", "B", "ROOT"}
        self.assertEqual(actual, expected)

    def test_ancestors_root(self):
        actual = ancestors("ROOT")
        expected = {"ROOT"}
        self.assertEqual(actual, expected)