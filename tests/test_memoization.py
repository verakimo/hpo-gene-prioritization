import unittest

from ontology import ancestors, ancestor_cache

class TestMemoization(unittest.TestCase):
    def test_ancestor_cache(self):
        ancestor_cache.clear()
        self.assertNotIn("D", ancestor_cache)
        ancestors("D")
        self.assertIn("D", ancestor_cache)
        actual = ancestor_cache["D"]
        expected = {"D", "A", "B", "ROOT"}
        self.assertEqual(actual, expected)
