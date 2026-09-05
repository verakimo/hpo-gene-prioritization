# Specification Document

## Programming Language

- The project uses Python as the programming language.

- For peer review, I am sufficiently proficient in Python to review projects written in it. I do not currently list any other programming language for peer review.

## Algorithms and Data Structures

The main algorithmic core consists of annotation propagation, Information Content calculation, MICA, Resnik semantic similarity, symmetric Best Match Average, and gene scoring and ranking. Jaccard similarity is used as a simple baseline for comparison.

The HPO ontology is represented as a directed acyclic graph (DAG). Python dictionaries and sets are used to store parent relations, gene-to-phenotype annotations, ancestor sets, Information Content values and cached results. Ancestor lookup uses graph traversal as a supporting operation, and memoization is used to avoid repeated ancestor calculations.

Information Content is calculated from propagated gene-to-phenotype annotations. For an HPO term $t$, the probability $p(t)$ is based on the proportion of genes associated with that term after annotation propagation, and

$$
IC(t) = -\log p(t).
$$

Resnik similarity is used for HPO term-to-term comparison, and symmetric Best Match Average aggregates the pairwise Resnik similarities into a phenotype-profile similarity score. The semantic similarity design is based on Resnik [1], biomedical ontology semantic similarity literature [2], and previous HPO-based gene prioritization work [3].

## Problem and Input Data of the Project

The computational problem of the project is to rank known disease-associated genes according to the similarity between a patient's phenotype profile and gene-associated phenotype profiles represented by HPO terms.

The program receives a set of HPO terms representing a patient phenotype profile. It also uses HPO ontology parent relations and gene-to-phenotype annotations. These data are used to calculate phenotype similarity scores for genes and produce a ranked list of candidate genes.

The main output is a ranked list of candidate genes together with their phenotype similarity scores.

A simple command-line interface supports providing the patient phenotype profile and viewing the ranking. Input parsing and the command-line interface support the algorithmic core but are not themselves part of the main algorithmic contribution.

## Scope

The project focuses on phenotype-based ranking of known gene candidates using HPO semantic similarity.

Variant-level analysis, VCF/BAM/FASTQ processing, variant calling, pathogenicity prediction, inheritance modelling, machine learning, natural-language processing, clinical diagnosis and a graphical user interface are outside the scope of the project.

## The Core of the Project

The core of the project is an ontology-based phenotype semantic similarity method for gene prioritization. The main algorithmic chain consists of annotation propagation, Information Content, MICA, Resnik similarity and symmetric Best Match Average. Jaccard similarity is implemented as a simple ontology-unaware baseline for comparison.

HPO graph traversal, parsing, caching and the command-line interface support the core but are not the main algorithmic contribution.

## Big-O Analysis

For the Big-O analysis of this project, the following notation is used:

- $V$ = number of HPO terms
- $E$ = number of ontology parent relations
- $|P|$ = number of HPO terms in the patient phenotype profile
- $|G|$ = maximum number of HPO terms in one gene phenotype profile used for scoring
- $N$ = number of genes in the gene-to-phenotype dataset used for Information Content calculation and ranking
- $A$ = total number of direct gene-to-phenotype annotations

Unless otherwise stated, the analysis assumes the standard average-case behaviour of Python hash-based dictionaries and sets.

The implementation uses a lazy ancestor cache. An uncached ancestor lookup may traverse the HPO graph in $O(V + E)$ time. Once an ancestor set is stored in the cache, retrieving it takes average $O(1)$ dictionary lookup time, assuming that the stored set is returned without copying. If ancestor sets are eventually requested for all $V$ terms, a conservative upper bound for constructing the complete cache is $O(V(V + E))$ time and $O(V^2)$ space.

Annotation propagation uses the cached ancestor sets. For each of the $A$ direct gene-to-phenotype annotations, up to $V$ HPO terms may need to be processed, giving an upper-bound time complexity of $O(AV)$. After propagation, Information Content values can be calculated from up to $NV$ propagated gene-term associations, giving $O(NV)$ time.

MICA and Resnik similarity use cached ancestor sets. Under the standard average-case assumptions for Python set operations, one MICA/Resnik term comparison has an $O(V)$ ontology-size upper bound.

For one candidate gene, symmetric Best Match Average compares every patient HPO term with every HPO term in the gene phenotype profile. This requires $|P||G|$ Resnik comparisons and therefore has a time complexity of

$$
O(|P||G|V).
$$

The implementation does not store the complete $|P| \times |G|$ similarity matrix. Instead, only the best matches needed for the symmetric average are retained. This gives an auxiliary-space estimate of

$$
O(|P| + |G| + V)
$$

for one BMA calculation with the current MICA design.

Jaccard similarity compares the phenotype term sets directly without using the HPO graph, MICA or Information Content. Its time complexity is $O(|P| + |G|)$ under the standard average-case assumptions for Python sets. The union does not need to be materialized because

$$
|P \cup G| = |P| + |G| - |P \cap G|,
$$

so the Jaccard calculation can use $O(1)$ additional space beyond the already existing phenotype sets.

After similarity scores have been calculated for the $N$ candidate genes, the gene-score pairs are sorted to produce the final ranking. Sorting requires $O(N \log N)$ time.

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

- The project documentation is written in English. Weekly reports may be written in Finnish.
