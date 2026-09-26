# User Guide

## Installation

Clone the repository and move to the project directory:

```bash
git clone https://github.com/verakimo/hpo-gene-prioritization.git
cd hpo-gene-prioritization
```

Install the dependencies with Poetry:

```bash
poetry install
```

## Required Data

The program requires two HPO data files. They are not included in the repository and must be downloaded separately.

### HPO ontology

Download `hp.obo` from:

[HPO ontology download](https://obofoundry.org/ontology/hp)

Place the file here:

```text
data/hp.obo
```

### Gene-to-phenotype annotations

Download `genes_to_phenotype.txt` from:

[Gene-to-phenotype annotations](https://obofoundry.org/ontology/hp)

Place the file here:

```text
data/genes_to_phenotype.txt
```

The expected structure is:

```text
data/
├── hp.obo
└── genes_to_phenotype.txt
```

## Running the Program

Run the program from the project root:

```bash
PYTHONPATH=src poetry run python src/main.py
```

The input is a patient phenotype profile consisting of valid **HPO IDs**.

For example:

```text
HP:0003707
HP:0003391
HP:0003551
```

The program compares the patient phenotype profile with gene-associated HPO profiles and prints the top-ranked candidate genes with their similarity scores.

## Running the Unit Tests

Run all unit tests:

```bash
PYTHONPATH=src poetry run python -m unittest discover -s tests -p "test_*.py" -v
```

For details about the test cases, coverage, and empirical validation, see the [Testing Document](documentation/testing_document.md).

## Test Coverage

Run branch coverage:

```bash
poetry run coverage erase
PYTHONPATH=src poetry run coverage run --branch --source=src -m unittest discover -s tests -p "test_*.py"
poetry run coverage report -m
```

## Pylint

Run Pylint for the source modules:

```bash
PYTHONPATH=src poetry run python -m pylint src
```

## Real-Case Validation

The empirical validation uses solved cases from the **Phenopacket Store**.

Download a Phenopacket Store release from:

[Phenopacket Store download link](https://github.com/monarch-initiative/phenopacket-store/releases/latest/download/all_phenopackets.zip)

Extract the downloaded release into:

```text
real_case_validation/benchmark_data/
```

For example, release `0.1.27` should have the following structure:

```text
real_case_validation/
├── benchmark_data/
│   └── 0.1.27/
│       ├── ABCA4/
│       ├── F8/
│       ├── GALT/
│       ├── OCA2/
│       └── ...
└── run_validation.py
```

The cohorts used in the validation are selected in `run_validation.py`:

```python
VALIDATION_COHORTS = (
    "ABCA4",
    "F8",
    "GALT",
    "OCA2"
)
```

Run the validation from the project root:

```bash
PYTHONPATH=src poetry run python real_case_validation/run_validation.py
```
