import unittest

from information_content import calculate_information_content

PROPAGATED_ANNOTATIONS = {
    "g1": {"C", "A", "ROOT"},
    "g2": {"D", "A", "B", "ROOT"},
    "g3": {"B", "ROOT"}
}

class TestInformationContent(unittest.TestCase):
    def test_calculate_information_content(self):
        actual = calculate_information_content(PROPAGATED_ANNOTATIONS)
        expected = {
            'ROOT': -0.0,
            'A': 0.5849625007211563,
            'C': 1.5849625007211563,
            'D': 1.5849625007211563,
            'B': 0.5849625007211563
        }
        self.assertEqual(actual.keys(), expected.keys())
        for term in expected:
            self.assertAlmostEqual(actual[term], expected[term])

    def test_calculate_information_content_for_empty_dataset(self):
        actual = calculate_information_content({})
        expected = {}
        self.assertEqual(actual, expected)