# Testing Document

## Unit Testing and Coverage

The algorithmic logic of the program is tested with Python's `unittest` framework. The current test suite contains **19 automated unit tests**, all of which pass.

Branch coverage is measured with the `coverage` package.

| Metric | Result |
|---|---:|
| Unit tests | 19 passed |
| Statements | 119 / 119 |
| Branches | 48 / 48 |
| Statement coverage | 100% |
| Branch coverage | 100% |

`main.py` contains the command-line interface and I/O and is excluded from the coverage calculation through `.coveragerc`. The tested algorithmic modules in `src` therefore have full statement and branch coverage.

The source modules in `src` were also checked with Pylint and received a score of **10.00/10**.

## What Was Tested and How?

The unit tests are divided into separate test modules corresponding to the main parts of the implementation. Small manually verifiable inputs are used so that the expected results can be checked independently.

- **HPO parsing (`test_hpo_parser.py`):** verifies that HPO term IDs and `is_a` parent relationships are parsed correctly. The parser is tested with one OBO fixture containing a `[Typedef]` section and another fixture that reaches the end of the file without one.
- **Gene annotation parsing (`test_gene_annotation_parser.py`):** verifies that gene symbols and HPO terms are read correctly from the gene-to-phenotype input file and stored in the expected gene-to-HPO mapping.
- **Ontology (`test_ontology.py`):** verifies ancestor lookup in a small ontology graph, including terms with multiple parent relationships.
- **Memoization (`test_memoization.py`):** verifies that ancestor sets calculated by the ontology are stored in the cache and reused in later queries.
- **Annotations (`test_annotations.py`):** verifies annotation propagation for a single gene. A gene with one direct HPO term is tested to ensure that the term and all of its ancestors are returned. A gene with multiple direct HPO terms is also tested to verify that the union of their ancestor sets is returned correctly.
- **Annotation propagation (`test_propagations.py`):** verifies propagation for a complete gene-to-phenotype annotation dataset. The expected propagated HPO terms are checked for every gene in a small manually constructed dataset. An empty annotation dataset is also tested and is expected to return an empty dictionary.
- **Information Content (`test_information_content.py`):** verifies that Information Content values are calculated correctly from propagated gene annotations.
- **Semantic similarity (`test_semantic_similarity.py`):** verifies MICA and Resnik similarity using a small manually constructed ontology. A disconnected ontology is also used to verify that a `ValueError` is raised when two HPO terms have no common ancestor.
- **Symmetric Best Match Average (`test_symmetric_bma.py`):** verifies that symmetric BMA returns the expected similarity score for a small patient phenotype profile and gene phenotype profile with manually defined IC values. It also verifies that a `ValueError` is raised when both phenotype profiles are empty or when the gene phenotype profile is empty.
- **Gene ranking (`test_gene_ranking.py`):** verifies gene scoring and that candidate genes are returned in the expected ranking order.

## Test Inputs

The automated unit tests use two main types of test inputs:

1. **Small file fixtures based on the formats of the real input data.**  
   Small OBO and gene-to-phenotype annotation files are used for testing the HPO parser and gene annotation parser. These files contain only the fields needed by the program and make the expected parser output easy to verify.

2. **Manually constructed test data.**  
   Small artificial ontology graphs, gene annotation sets, and phenotype profiles are created specifically for testing the algorithmic logic. They are used to test ancestor lookup, annotation propagation, Information Content, MICA and Resnik similarity, profile similarity, and gene ranking.

The manually constructed inputs are intentionally small so that the expected results can be calculated or checked by hand.

## Empirical Validation

In addition to unit testing, the complete prioritization pipeline was tested using real solved cases from the **Phenopacket Store**.

Phenopacket Store: [GitHub repository link](https://github.com/monarch-initiative/phenopacket-store/tree/main)

Download link: [download link](https://github.com/monarch-initiative/phenopacket-store/releases/latest/download/all_phenopackets.zip)

Four cohorts were selected for the validation: **ABCA4, F8, GALT, and OCA2**.

For each solved case, the program:

1. reads the Phenopacket JSON file;
2. extracts the present HPO terms;
3. verifies that the interpretation is marked as solved;
4. extracts the known causal gene;
5. runs the complete phenotype-based gene-prioritization pipeline;
6. records the rank of the causal gene.

| Causal gene | Cases | Ranked #1 | Ranked #1 (%) | Top 10 | Top 10 (%) |
|---|---:|---:|---:|---:|---:|
| ABCA4 | 6 | 0 | 0.00% | 4 | 66.67% |
| F8 | 8 | 6 | 75.00% | 8 | 100.00% |
| GALT | 1 | 1 | 100.00% | 1 | 100.00% |
| OCA2 | 1 | 0 | 0.00% | 0 | 0.00% |
| **TOTAL** | **16** | **7** | **43.75%** | **13** | **81.25%** |

The known causal gene was ranked **first in 7/16 cases (43.75%)** and **within the top 10 in 13/16 cases (81.25%)**.

The validation processed all 16 cases in **16.10 seconds**, with an average runtime of approximately **1.01 seconds per case**.

The percentages are not interpreted as a general accuracy estimate of the method. The validation set is small and unbalanced: 8 of the 16 cases belong to the F8 cohort. The purpose of the experiment is to verify that the complete implementation can prioritize known causal genes using real solved patient phenotype data.

## Reproducing the Tests

Run the unit tests:

```bash
PYTHONPATH=src poetry run python -m unittest discover -s tests -p "test_*.py" -v
```

Run branch coverage:

```bash
poetry run python -m coverage erase
PYTHONPATH=src poetry run python -m coverage run --branch --source=src -m unittest discover -s tests -p "test_*.py"
poetry run python -m coverage report -m
```

Run Pylint:

```bash
PYTHONPATH=src poetry run python -m pylint src
```

Run the empirical validation:

```bash
PYTHONPATH=src poetry run python real_case_validation/run_validation.py
```
