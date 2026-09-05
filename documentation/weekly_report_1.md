# Weekly Report 1

## What did I do this week?

- I decided on the topic of the project. Since the course allows students to choose their own topic, I wanted to work on something related to bioinformatics and systems medicine. I used ChatGPT to help narrow the initial idea into a scope that is more suitable for this course.

- I familiarized myself with the main terminology of the project, especially concepts related to the Human Phenotype Ontology (HPO).

- I wrote the first version of the Specification Document and Weekly Report 1.

- I reviewed Chapters 1, 3 and 4 of the *Tietorakenteet ja algoritmit I* course in order to refresh the concepts needed for the data structures and complexity analysis used in this project.

- I worked through the expected time and space complexities of the main algorithms and operations in the project. My initial notes on the Big-O analysis became about four pages long, so I later shortened the analysis considerably for the Specification Document and summarized the main results in a table.

- I also wrote approximately three A4 pages of handwritten notes about the project. This helped me organize the algorithmic pipeline and understand the new material more clearly.

- I used relevant Wikipedia articles for initial orientation and, with the help of ChatGPT, identified three main scientific articles for the project. These will serve as the main starting points for the literature review.

## How has the project progressed?

The project has progressed more slowly toward implementation than I initially expected, because most of this week was spent on understanding the problem, defining the scope and working through the complexity analysis. I have not started the actual implementation yet, but the computational problem, the main algorithmic components and the planned data structures are now much clearer than at the beginning of the week.

## What did I learn this week?

- I learned the main terminology needed for the project, especially concepts related to HPO and phenotype-based gene prioritization.

- I worked through the role of each major algorithmic component in the planned pipeline, including annotation propagation, Information Content, MICA, Resnik similarity, symmetric Best Match Average and the Jaccard baseline.

- I practiced deriving time and space complexity estimates from the structure of an algorithm and from the data structures used in its implementation. This helped me understand Big-O analysis better than simply memorizing complexity results.

- I also learned that some complexity estimates depend on implementation choices. For example, caching ancestor sets trades additional memory for faster repeated lookups, and BMA can be implemented without storing the complete pairwise similarity matrix.

## What remains unclear or has been challenging?

There are still a few questions I would like to clarify:

- Is the current topic and scope suitable for the course, particularly the choice of Information Content, MICA, Resnik similarity and symmetric Best Match Average as the main algorithmic core?

- I already have a more detailed Big-O analysis than what is included in the Specification Document. Would it be useful to include this as a separate project document now, or is it better to keep it as working material and later revise it for the implementation documentation after the implementation choices are clearer?

- Since this is my first project with several interacting algorithmic components, I am not yet sure what the most sensible first implementation step would be. Would you recommend starting with the HPO graph and ancestor lookup, or approaching the implementation in another order?

## What will I do next?

Next, I plan to move from specification to implementation. I will start with a small controlled toy version of the HPO graph rather than immediately using the full HPO dataset. The first goal is to represent a small HPO DAG and implement the basic ontology structure needed for ancestor lookup. This should make it possible to test the basic graph operations before adding the later semantic-similarity components.

## Time spent

I spent **13 hours and 15 minutes** on the course this week.
