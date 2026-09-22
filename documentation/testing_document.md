# Testing Documentation

## Unit tests

The project is tested with Python's `unittest` framework.

Name                            Stmts   Miss Branch BrPart  Cover   Missing
---------------------------------------------------------------------------
src/annotations.py                 11      0      4      0   100%
src/gene_annotation_parser.py      12      0      4      0   100%
src/gene_ranking.py                17      0      4      0   100%
src/hpo_parser.py                  12      0      8      0   100%
src/information_content.py         11      0      6      0   100%
src/main.py                        35     35      6      0     0%   10-67
src/ontology.py                    17      0      6      0   100%
src/profile_similarity.py          22      0     10      0   100%
src/semantic_similarity.py         17      0      6      0   100%
---------------------------------------------------------------------------
TOTAL                             154     35     54      0    80%
Current total branch coverage: **80%**.

## Code quality

Code quality is checked with Pylint:

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

Current Pylint score: **9.81/10**.