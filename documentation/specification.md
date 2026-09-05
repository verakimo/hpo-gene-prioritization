# Specification Document

## Programming Language

- The project uses Python as the programming language.

- For peer review, I am sufficiently proficient in Python to review projects written in it. I do not currently list any other programming language for peer review.

## Algorithms and Data Structures
The main algorithmic core consists of annotation propagation, Information Content calculation, MICA, Resnik semantic similarity, symmetric Best Match Average, and gene scoring/ranking. Jaccard similarity is implemented as a baseline. The HPO ontology is represented as a directed acyclic graph (DAG). Python dictionaries and sets are used to store parent relations, gene-to-phenotype annotations, ancestor sets and cached results. Ancestor lookup uses graph traversal as a supporting operation.

## Problem and Input Data of the Project
- The problem my project aims to solve is ranking known disease-associated genes according to the similarity between a patient's phenotype profile and gene-associated phenotype profiles represented by HPO terms.
- The program will receive a set of HPO terms representing a patient phenotype profile. It will also use HPO ontology parent relations and gene-to-phenotype annotations. These data will be used to calculate phenotype similarity scores for genes and produce a ranked list of candidate genes.

## Scope

The project focuses on phenotype-based ranking of known gene candidates using HPO semantic similarity.

Variant-level analysis, VCF/BAM/FASTQ processing, variant calling, pathogenicity prediction, inheritance modelling, machine learning, natural-language processing, clinical diagnosis and a graphical user interface are outside the scope of the project.

## The Core of the Project

The core of the project is an ontology-based phenotype semantic similarity method for gene prioritization based on Information Content, MICA, Resnik similarity and symmetric Best Match Average. Jaccard similarity is used as a simple ontology-unaware baseline. Graph traversal, parsing, caching and the command-line interface are supporting components rather than the main algorithmic contribution.

## Big-O Analysis

For the Big-O analysis of this project, the following notation is used:

- $V$ = number of HPO terms
- $E$ = number of ontology parent relations
- $|P|$ = number of HPO terms in the patient phenotype profile
- $|G|$ = maximum number of HPO terms in one gene phenotype profile used for scoring
- $N$ = number of genes in the gene-to-phenotype dataset used for Information Content calculation and ranking
- $A$ = total number of direct gene-to-phenotype annotations

Unless otherwise stated, the analysis assumes the standard average-case behaviour of Python hash-based dictionaries and sets.

The HPO ontology is represented as a DAG with $V$ terms and $E$ parent relations, so reading and storing the graph requires $O(V + E)$ time and space. An uncached ancestor lookup may also require $O(V + E)$ time. Ancestor sets are memoized; cached retrieval takes average $O(1)$ time, while storing ancestor sets for all terms may require up to $O(V^2)$ space. A conservative upper bound for constructing the complete cache is $O(V(V + E))$ time.

Annotation propagation processes the ancestors of each of the $A$ direct gene-to-phenotype annotations, giving an upper-bound time complexity of $O(AV)$. Information Content calculation processes the propagated gene-term associations and therefore requires up to $O(NV)$ time.

With cached ancestor sets, MICA and Resnik similarity have an $O(V)$ ontology-size upper bound under the standard average-case assumptions for Python set operations. Symmetric Best Match Average compares every patient term with every term in one gene phenotype profile, requiring $|P||G|$ Resnik comparisons. Its time complexity is therefore $O(|P||G|V)$. The implementation stores only the best matches rather than the complete similarity matrix, giving $O(|P| + |G| + V)$ auxiliary space for one BMA calculation.

Jaccard similarity is used as an ontology-unaware baseline and requires $O(|P| + |G|)$ time and $O(1)$ additional space beyond the existing phenotype sets. Scoring all $N$ candidate genes with the semantic method requires $O(N|P||G|V)$ time, after which sorting the gene-score pairs requires $O(N \log N)$ time.

### Complexity Summary

The following table summarizes the expected complexities of the main components. The estimates involving Python dictionaries and sets assume their standard average-case hash-table behaviour.

| Component | Time Complexity | Space Complexity |
| --- | --- | --- |
| Build/read HPO DAG | $O(V + E)$ | $O(V + E)$ |
| Ancestor lookup, uncached | $O(V + E)$ | $O(V)$ auxiliary |
| Ancestor cache retrieval | average $O(1)$ | cache up to $O(V^2)$ |
| Complete ancestor-cache construction | conservative upper bound $O(V(V + E))$ | up to $O(V^2)$ |
| Annotation propagation | $O(AV)$ | up to $O(NV)$ |
| Information Content calculation | $O(NV)$ | $O(V)$ auxiliary |
| MICA | $O(V)$ | $O(V)$ auxiliary if the intersection is materialized |
| Resnik similarity | $O(V)$ | $O(V)$ auxiliary with the current MICA design |
| Symmetric BMA for one gene | $O(\lvert P \rvert \lvert G \rvert V)$ | $O(\lvert P \rvert + \lvert G \rvert + V)$ auxiliary |
| Jaccard similarity for one gene | $O(\lvert P \rvert + \lvert G \rvert)$ | $O(1)$ auxiliary |
| Semantic scoring of all candidate genes | $O(N \lvert P \rvert \lvert G \rvert V)$ | $O(N + \lvert P \rvert + \lvert G \rvert + V)$ auxiliary |
| Gene ranking | $O(N \log N)$ | $O(N)$ auxiliary |

## References

[1] Resnik, P. (1995). ‘Using Information Content to Evaluate Semantic Similarity in a Taxonomy’. In: *Proceedings of the 14th International Joint Conference on Artificial Intelligence (IJCAI)*, Vol. 1, pp. 448–453.

[2] Pesquita, C., Faria, D., Falcão, A.O., Lord, P. and Couto, F.M. (2009). ‘Semantic Similarity in Biomedical Ontologies’. *PLOS Computational Biology*, 5(7), e1000443. doi:10.1371/journal.pcbi.1000443.

[3] Masino, A.J., Dechene, E.T., Dulik, M.C., Wilkens, A., Spinner, N.B., Krantz, I.D., Pennington, J.W., Robinson, P.N. and White, P.S. (2014). ‘Clinical phenotype-based gene prioritization: an initial study using semantic similarity and the Human Phenotype Ontology’. *BMC Bioinformatics*, 15, 248. doi:10.1186/1471-2105-15-248.

[4] Human Phenotype Ontology (HPO) (2026). *Human Phenotype Ontology documentation*. Available at: https://obophenotype.github.io/human-phenotype-ontology/ (Accessed: 4 September 2026).

## Other Notes

- I study in the Bachelor's Programme in Computer Science (TKT).

- The project documentation and weekly reports will be written in English.
