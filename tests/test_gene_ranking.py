import unittest

from gene_ranking import score_genes, rank_genes, rich_output
from ontology import Ontology

PATIENT_PROFILE = {"C", "B"}

GENE_PROFILES = {
    "g1": {"C"},
    "g2": {"D", "A"},
    "g3": {"B"}
}

IC_VALUES = {
    'ROOT': -0.0,
    'A': 0.5849625007211563,
    'C': 1.5849625007211563,
    'D': 1.5849625007211563,
    'B': 0.5849625007211563
    }

GENE_SCORES = {
    'g1': 1.1887218755408673,
    'g2': 0.5849625007211563,
    'g3': 0.4387218755408672
}

UNRANKED_GENE_SCORES = {
    'g3': 0.4387218755408672,
    'g1': 1.1887218755408673,
    'g2': 0.5849625007211563
}

TOY_PARENTS = {
    "ROOT": set(),
    "A": {"ROOT"},
    "B": {"ROOT"},
    "C": {"A"},
    "D": {"A", "B"}
}


class TestGeneRanking(unittest.TestCase):
    def setUp(self):
        self.ontology = Ontology(TOY_PARENTS)

    def test_score_genes(self):
        actual = score_genes(PATIENT_PROFILE, GENE_PROFILES, IC_VALUES, self.ontology)
        expected = {
            'g1': 1.1887218755408673,
            'g2': 0.5849625007211563,
            'g3': 0.4387218755408672
            }
        self.assertEqual(actual, expected)

    def test_rank_genes(self):
        actual = rank_genes(UNRANKED_GENE_SCORES)
        self.assertEqual(list(actual.keys()), ["g1", "g2", "g3"])

    def test_rich_output(self):
        actual = rich_output(GENE_SCORES, GENE_PROFILES)
        expected = [
            {
                'rank': 1,
                'gene': 'g1',
                'score': 1.1887218755408673,
                'phenotypes': {'C'}
            },
            {
                'rank': 2,
                'gene': 'g2',
                'score': 0.5849625007211563,
                'phenotypes': {'A', 'D'}
            },
            {
                'rank': 3,
                'gene': 'g3',
                'score': 0.4387218755408672,
                'phenotypes': {'B'}
            }
        ]
        self.assertEqual(actual, expected)
    