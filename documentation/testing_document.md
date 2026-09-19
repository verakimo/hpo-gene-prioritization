# Testing Documentation

## Unit tests

The project is tested with Python's `unittest` framework.

Name                            Stmts   Miss Branch BrPart  Cover   Missing
---------------------------------------------------------------------------
src/annotations.py                 11      0      4      0   100%
src/gene_annotation_parser.py      12      0      4      0   100%
src/gene_ranking.py                17      0      4      0   100%
src/hpo_parser.py                  12      0      8      1    95%   14->22
src/information_content.py         11      0      6      0   100%
src/main.py                        35     35      6      0     0%   1-56
src/ontology.py                    17      0      6      0   100%
src/profile_similarity.py          29      0     12      0   100%
src/semantic_similarity.py         17      1      6      1    91%   23
---------------------------------------------------------------------------
TOTAL                             161     36     56      2    80%
Current total branch coverage: **80%**.

## Code quality

Code quality is checked with Pylint:

************* Module main
src/main.py:23:0: C0301: Line too long (131/100) (line-too-long)
src/main.py:1:0: C0114: Missing module docstring (missing-module-docstring)
src/main.py:14:0: C0116: Missing function or method docstring (missing-function-docstring)

-------------------------------------------------------------------
Your code has been rated at 9.81/10 (previous run: 10.00/10, -0.19)

Current Pylint score: **9.81/10**.