import unittest

from gene_annotation_parser import parse_gene_annotations

FILE_PATH = "tests/test_data/test_gene_to_phenotype.txt"

class TestGeneAnnotationParser(unittest.TestCase):
    def test_gene_annotation_parser(self):
        actual = parse_gene_annotations(FILE_PATH)
        expected = {
            "NAT2": {"HP:0000007", "HP:0001939"},
            "AARS1": {"HP:0002460", "HP:0002451", "HP:0008619"},
            "SALL1": {"HP:0011304", "HP:0004322", "HP:0030676", "HP:0030680", "HP:0000772"},
            "CEP152": {"HP:0001249"},
            "TMEM43": {"HP:0003306", "HP:0004631", "HP:0011807"}
        }
        self.assertEqual(actual, expected)