# Weekly Report 3

## What did I do this week?

- I wrote three Python files containing the main algorithms of the project:
  - `semantic_similarity.py`
  - `profile_similarity.py`
  - `gene_ranking.py`

- I implemented MICA, Resnik semantic similarity, symmetric Best Match Average (BMA), gene scoring and gene ranking.

- I refactored the ontology part of the program. Earlier the functions depended directly on the toy ontology. I created an `Ontology` class, so now the same algorithms can work with different ontology graphs instead of only the toy data.

- Because of this refactoring, I also had to modify the functions that use the ontology and update the related unit tests.

- I wrote two parsers:
  - `hpo_parser.py` for reading the HPO ontology from `hp.obo`
  - `gene_annotation_parser.py` for reading gene-to-phenotype annotations from `genes_to_phenotype.txt`

- I added `main.py`, which provides a simple runnable interface. The user can enter the patient's phenotype terms as HPO IDs, and the program returns the top ranked gene candidates. The output currently shows the rank, similarity score, number of direct phenotype annotations and exact matches between the patient input and the gene annotations.

- I connected the program to real HPO data and successfully ran the whole pipeline:

  `HPO data -> annotation propagation -> Information Content -> Resnik -> BMA -> gene scoring -> gene ranking`

- I wrote about 20 new unit tests for the new functionality and parsers.

- I added docstrings to the source files, except for `main.py`, which still needs documentation.

- I configured Poetry for the project.

- I used Pylint and coverage to check the code. The current test coverage is about **80%**, and the current Pylint score is **9.81/10**.

- I read the reference literature related to semantic similarity and HPO.

- I had a Zoom meeting.

- I wrote about five A4 pages of my own notes about the project concepts, implementation and Poetry.

- I started writing the testing document.

## How has the program progressed?

I think the main functionality of the project is now close to being complete.

The program no longer works only with manually created toy data. It can read the real HPO ontology and real gene-to-phenotype annotations, calculate semantic similarities and rank genes based on a patient's HPO phenotype profile.

I have also tested the complete pipeline with real HPO data. The next important step is to test it with solved rare-disease cases where the causal gene is already known.

## What did I learn this week?

- I learned how to implement semantic similarity algorithms such as MICA, Resnik similarity and symmetric BMA.

- I learned how to refactor code so that the algorithms are not tied to one global toy dataset.

- I learned how OBO files are structured and how to parse the `id` and `is_a` relations from `hp.obo`.

- I learned how to install and use Poetry in the correct Python environment.

- I also learned that exact HPO term overlap and semantic similarity are not the same thing. A gene can have fewer exact matches with the patient's HPO terms but still receive a higher BMA score if its phenotype profile is semantically more similar overall.

- I found that real solved rare-disease cases can be used as benchmark data. In these cases the causal gene is already known, so I can check how highly my program ranks it (link: https://github.com/monarch-initiative/phenopacket-store/tree/main).

## What remains unclear or has been challenging?

The most challenging part was the ontology refactoring. At first the ontology traversal depended directly on the toy graph. After introducing the `Ontology` class, I had to pass the ontology object through several parts of the program and also modify many unit tests.

Another challenge was fixing code quality issues found by Pylint and making the code work with the real HPO datasets instead of only controlled toy examples.

One question is still unclear to me:

The original plan included comparing the HPO semantic-similarity method with a Jaccard baseline. At this point, the project already implements the complete phenotype-driven gene-prioritization pipeline from scratch: HPO parsing and traversal, annotation propagation, Information Content, MICA/Resnik similarity, symmetric BMA, real HPO gene annotations, gene ranking, tests, and a runnable interface.

Would you consider this sufficient experimental and algorithmic scope for the course project, so that the Jaccard comparison could be left out and the remaining time could instead be used for testing the ranking with real solved rare-disease cases?

## What will I do next?

- Test the gene ranking with real solved rare-disease cases where the causal gene is known.
- Continue the testing document.
- Start the implementation document.
- Add documentation to `main.py`.
- Possibly add tests for the runnable interface.
- Improve the presentation of the results if there is enough time.

## Time spent

This week I spent **16 hours and 30 minutes** working on the course project.