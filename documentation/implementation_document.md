# Implementation Document

## General Structure of the Program

The program is implemented in Python as a pipeline for phenotype-driven gene prioritization. It reads the HPO ontology and gene-to-phenotype annotation data, represents the ontology using parent relationships and cached ancestor sets, propagates gene annotations to ancestor HPO terms, calculates Information Content values, computes pairwise semantic similarity using MICA and Resnik similarity, combines these scores with symmetric Best Match Average, and finally ranks candidate genes according to their similarity to the patient's HPO phenotype profile. The implementation is divided into separate modules for ontology parsing and traversal, annotation parsing and propagation, Information Content, semantic similarity, profile similarity, gene ranking, and the command-line interface.

## Time and Space Complexity

The ontology is represented as a graph. An uncached ancestor search using DFS takes O(V + E) time in the worst case, where V is the number of HPO terms and E is the number of ontology edges. Memoization avoids repeating searches for previously processed terms.

With cached ancestor sets, MICA and Resnik take up to O(V) time per term pair. Symmetric BMA compares patient and gene phenotype terms in both
directions. Scoring all genes takes O(P × S × V) time, where P is the number of patient terms and S is the total number of terms across all gene profiles. Sorting N genes takes O(N log N) time.

The ontology requires O(V + E) space. Cached ancestor sets may require up to O(V²) additional space, propagated gene annotations require O(S), and the gene ranking output requires O(N).

## Shortcomings and Possible Improvements

The program prioritizes candidate genes based on phenotypic similarity, but it does not identify specific disease-causing alleles or genetic variants. A possible future improvement would be to integrate genetic variant data and extend the program to variant-level prioritization.

## Use of Large Language Models and AI Tools

**ChatGPT** was used to support learning and project development:
- Finding relevant literature and other sources.
- Explaining terminology and technical questions, including time and space complexity, Poetry installation, and Pylint errors.
- Translating texts into English and correcting grammatical errors.
- Shortening the specification document.
- Formatting documentation in Markdown.

**DeepL** was used to translate individual words in the project's docstrings.

**AI Tutor (Python Tutor)** was used to understand a bug in the `information_content()` function.

**GitHub Copilot** was used to generate commit messages when making changes directly on GitHub.

The code was written entirely by me, without using LLM-generated code.

## References

[1] P. Resnik, "Using Information Content to Evaluate Semantic
Similarity in a Taxonomy," in *Proceedings of the 14th International
Joint Conference on Artificial Intelligence (IJCAI)*, vol. 1,
pp. 448–453, 1995.
Available: https://arxiv.org/abs/cmp-lg/9511007

[2] C. Pesquita, D. Faria, A. O. Falcão, P. Lord, and F. M. Couto,
"Semantic Similarity in Biomedical Ontologies,"
*PLoS Computational Biology*, vol. 5, no. 7, e1000443, 2009.
doi: 10.1371/journal.pcbi.1000443

[3] A. J. Masino et al., "Clinical phenotype-based gene
prioritization: An initial study using semantic similarity
and the human phenotype ontology," *BMC Bioinformatics*,
vol. 15, art. no. 248, 2014.
doi: 10.1186/1471-2105-15-248

[4] M. S. Ladewig et al., "GA4GH Phenopackets: A Practical
Introduction," *Advanced Genetics*, vol. 4, no. 1,
art. no. 2200016, 2023.
doi: 10.1002/ggn2.202200016

[5] OBO Foundry, "Human Phenotype Ontology (HPO)." [Online].
Available: https://obofoundry.org/ontology/hp

[6] Human Phenotype Ontology, "Gene-to-Phenotype Annotations."
[Online].
Available: https://obophenotype.github.io/human-phenotype-ontology/annotations/genes_to_phenotype/

[7] Monarch Initiative, "Phenopacket Store," GitHub repository.
[Online].
Available: https://github.com/monarch-initiative/phenopacket-store

[8] University of Helsinki, "Data Structures and Algorithms,
Spring 2026." [Online].
Available: https://tira.mooc.fi/kevat-2026/

[9] University of Helsinki, "Python Programming MOOC 2026:
Writing Files." [Online].
Available: https://ohjelmointi-26.mooc.fi/osa-6/2-tiedostojen-kirjoittaminen

[10] University of Helsinki, "Algorithms and Artificial
Intelligence Lab." [Online].
Available: https://algolabra-hy.github.io/

[11] University of Helsinki, "Software Engineering."
[Online].
Available: https://ohjelmistotuotanto-hy.github.io/

[12] DataCamp, "DataCamp." [Online].
Available: https://www.datacamp.com/

[13] GeeksforGeeks, "GeeksforGeeks." [Online].
Available: https://www.geeksforgeeks.org/

[14] W3Schools, "W3Schools." [Online].
Available: https://www.w3schools.com/
