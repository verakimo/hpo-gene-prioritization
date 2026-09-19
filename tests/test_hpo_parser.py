import unittest

from hpo_parser import parse_obo

FILE_PATH = "tests/test_data/test_hp.obo"

class TestHPOParser(unittest.TestCase):
    def test_hpo_parser(self):
        actual = parse_obo(FILE_PATH)
        expected = {
            "HP:0000001": set(),
            "HP:0000002": {"HP:0001507"},
            "HP:0000003": {"HP:0000107"},
            "HP:0000005": {"HP:0000001"},
            "HP:0000006": {"HP:0034345"},
            "HP:0000007": {"HP:0034345"},
            "HP:0000008": {"HP:0000812", "HP:0010460"},
            "HP:0000009": {"HP:0000014"},
            "HP:0000010": {"HP:0002719", "HP:5210135"},
            "HP:0000011": {"HP:0000009"},
            "HP:0000012": {"HP:0000009"},
            "HP:0000013": {"HP:0008684"},
            "HP:0000014": {"HP:0010936"},
            "HP:0000015": {"HP:0025487"},
            "HP:0000016": {"HP:0000009"}
        }
        self.assertEqual(actual, expected)