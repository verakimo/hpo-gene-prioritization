## General Structure of the Program

The program is implemented in Python as a pipeline for phenotype-driven gene prioritization. It takes a patient's HPO phenotype profile as input and processes the HPO ontology and gene-to-phenotype annotation data. The ontology is represented using parent relationships and cached ancestor sets. Gene annotations are propagated to ancestor HPO terms, Information Content (IC) values are calculated, and semantic similarity is computed using Most Informative Common Ancestor (MICA), Resnik similarity, and symmetric Best Match Average (BMA). Finally, candidate genes are sorted according to their similarity to the patient's phenotype profile.

The program can be divided into three main stages:  
1. reading and preprocessing the data,  
2. calculating semantic similarity between the patient phenotype profile and gene phenotype profiles, and  
3. sorting candidate genes and presenting the results to the user.

### 1. Data Reading and Preprocessing

First, `main.py` checks the user's input and the availability of the required `hp.obo` and `genes_to_phenotype.txt` data files [1-2].

In `hpo_parser.py`, the HPO ontology is parsed from `hp.obo` into a representation of a Directed Acyclic Graph (DAG). The ontology is stored as a dictionary that maps each HPO term to a set of its direct parent terms [1].

In `gene_annotation_parser.py`, the `genes_to_phenotype.txt` file is parsed into a dictionary that maps each gene to a set of directly annotated HPO terms [1-2].

The `Ontology` class in `ontology.py` uses Depth-First Search (DFS) to find all ancestors of an HPO term up to the root of the ontology (the root of the DAG). Previously calculated ancestor sets are cached to avoid repeating the same searches [3].

In `annotation_propagation.py`, the direct HPO annotations of each gene are propagated so that the gene profile also contains the ancestors of its directly annotated terms.

Finally, `information_content.py` calculates the IC value of every HPO term using

$$
IC(t) = -\log_2 p(t),
$$

where

$$
p(t) =
\frac{\text{number of genes annotated to } t}
{\text{total number of annotated genes}}.
$$

The gene counts are based on the propagated gene annotations [4].

### 2. Semantic Similarity

The second stage compares the patient's HPO phenotype profile with the propagated phenotype profile of each gene.

In `semantic_similarity.py`, Resnik similarity is calculated for pairs of HPO terms. For two terms, their Most Informative Common Ancestor is selected from their common ancestors. The MICA is the common ancestor with the highest IC value. Resnik similarity is then defined as the IC value of this MICA [4-5].

To compare complete phenotype profiles, the program uses symmetric BMA [5-6]:

$$
BMA(P,G) =
\frac{1}{2}
\left(
\frac{1}{|P|}
\sum_{p \in P}
\max_{g \in G} Resnik(p,g)
+
\frac{1}{|G|}
\sum_{g \in G}
\max_{p \in P} Resnik(p,g)
\right),
$$

where $P$ is the patient's phenotype profile and $G$ is the gene phenotype profile.

The first directional average finds the best matching gene term for every patient term, while the second finds the best matching patient term for every gene term. Their average gives the final symmetric BMA score. This score represents how similar a gene's phenotype profile is to the patient's phenotype profile.

### 3. Gene Prioritization and Output

In `gene_ranking.py`, a BMA score is calculated for every candidate gene. The scores are stored in a dictionary that maps each gene to its BMA score, and the genes are then sorted in descending order of similarity.

The ranked results are enriched with the gene's rank, BMA score, and phenotype annotations. Finally, `main.py` formats the results into a user-friendly command-line output and displays the ten highest-ranked candidate genes for the phenotype profile provided by the user.

### Implementation Resources

The implementation of the program was supported by several learning resources, including course materials from the University of Helsinki courses *Data Structures and Algorithms, Spring 2026* [3], *Introduction to Programming, 2026* [7], *Algorithms and Artificial Intelligence Project* [8], and *Software Engineering* [9], as well as the programming resources listed in references [10–12].

The scientific literature in references [4]–[6] was used to understand the theoretical background and core algorithms used in the project, including Information Content, Resnik similarity, and phenotype-based gene prioritization.

For the real-case validation, GA4GH Phenopacket resources [13] and data from the Phenopacket Store [14] were used. See the [Testing Document](testing_document.md) for more details.

## Time and Space Complexity

The ontology is represented as a DAG. An uncached ancestor search using DFS takes O(V + E) time in the worst case, where V is the number of HPO terms and E is the number of ontology edges. Memoization avoids repeating searches for previously processed terms.

With cached ancestor sets, MICA and Resnik take up to O(V) time per term pair. Symmetric BMA compares patient and gene phenotype terms in both
directions. Scoring all genes takes O(P × S × V) time, where P is the number of patient terms and S is the total number of terms across all gene profiles. Sorting N genes takes O(N log N) time.

The ontology requires O(V + E) space. Cached ancestor sets may require up to O(V²) additional space, propagated gene annotations require O(S), and the gene ranking output requires O(N).

## Shortcomings and Possible Improvements

The program prioritizes candidate genes based on phenotypic similarity, but it does not identify specific disease-causing alleles or genetic variants. A possible future improvement would be to integrate genetic variant data and extend the program to variant-level prioritization.

Another possible extension would be to include a gene-to-disease annotation file, such as `genes_to_disease.txt`, so that the program could also return candidate disease names based on the patient's phenotype profile.

The output could also be extended so that the ranked results could be saved to a file, for example in `.txt` or `.json` format, instead of being displayed only in the command-line interface.

## Use of Large Language Models and AI Tools

**ChatGPT** was used to support learning and project development:
- Finding relevant literature and other sources.
- Explaining terminology and technical questions.
- Working with texts: translating between languages, checking grammar, shortening, and polishing.
- Formatting documentation in Markdown.
- Formatting references in IEEE style.

**DeepL** was used a few times to translate individual words in the project's docstrings.

**AI Tutor (Python Tutor)** was used to understand a bug in the `information_content()` function.

**GitHub Copilot** was used to generate commit messages when making changes directly on GitHub.

The code was written entirely by me, without using LLM-generated code.

## References

[1] OBO Foundry, "Human Phenotype Ontology (HPO)." [Online].
Available: https://obofoundry.org/ontology/hp

[2] Human Phenotype Ontology, "Gene-to-Phenotype Annotations."
[Online].
Available: https://obophenotype.github.io/human-phenotype-ontology/annotations/genes_to_phenotype/

[3] University of Helsinki, "Data Structures and Algorithms,
Spring 2026." [Online].
Available: https://tira.mooc.fi/kevat-2026/

[4] P. Resnik, "Using Information Content to Evaluate Semantic
Similarity in a Taxonomy," in *Proceedings of the 14th International
Joint Conference on Artificial Intelligence (IJCAI)*, vol. 1,
pp. 448–453, 1995.
Available: https://arxiv.org/pdf/cmp-lg/9511007

[5] C. Pesquita, D. Faria, A. O. Falcão, P. Lord, and F. M. Couto,
"Semantic Similarity in Biomedical Ontologies,"
*PLoS Computational Biology*, vol. 5, no. 7, e1000443, 2009.
doi: 10.1371/journal.pcbi.1000443

[6] A. J. Masino et al., "Clinical phenotype-based gene
prioritization: An initial study using semantic similarity
and the human phenotype ontology," *BMC Bioinformatics*,
vol. 15, art. no. 248, 2014.
doi: 10.1186/1471-2105-15-248

[7] University of Helsinki, "Python Programming MOOC 2026:
Data Processing." [Online].
Available: https://ohjelmointi-26.mooc.fi/osa-7/4-datan-kasittely

[8] University of Helsinki, "Algorithms and Artificial Intelligence Project." [Online].
Available: https://algolabra-hy.github.io/

[9] University of Helsinki, "Software Engineering."
[Online].
Available: https://ohjelmistotuotanto-hy.github.io/

[10] DataCamp, "DataCamp." [Online].
Available: https://www.datacamp.com/

[11] GeeksforGeeks, "GeeksforGeeks." [Online].
Available: https://www.geeksforgeeks.org/

[12] W3Schools, "W3Schools." [Online].
Available: https://www.w3schools.com/

[13] M. S. Ladewig et al., "GA4GH Phenopackets: A Practical
Introduction," *Advanced Genetics*, vol. 4, no. 1,
art. no. 2200016, 2023.
doi: 10.1002/ggn2.202200016

[14] Monarch Initiative, "Phenopacket Store," GitHub repository.
[Online].
Available: https://github.com/monarch-initiative/phenopacket-store
