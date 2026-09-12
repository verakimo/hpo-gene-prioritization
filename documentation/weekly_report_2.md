# Weekly Report 2

## What did I do this week?

- I wrote three Python files containing the current core implementation: `ontology.py`, `annotations.py`, and `information_content.py`.
- I wrote seven unit tests covering `ancestors()`, `annotation()`, `propagation()`, and ancestor-cache memoization.
- I added docstrings to all implemented functions.
- I reviewed Chapters 5, 7, 8, 10, and 13 of the Tietorakenteet ja algoritmit course materials.
- I tested the implemented functionality using unit tests, except for `information_content()`, for which I have not yet written unit tests.
- I reviewed the course material on unit testing before writing my first unit tests.
- I wrote about five A4 pages of handwritten notes. These included manual calculations for the toy data and the expected results of the main algorithms used in the project.

## How has the program progressed?

In my opinion, the project progressed well this week, especially in terms of implementation. I now have working code for ancestor lookup, memoization, annotation propagation, and Information Content calculation on the toy data.

## What did I learn this week?

- I learned how to write and run unit tests using Python's `unittest` framework.
- I learned how to write docstrings based on the course materials, using the Google-style format.
- I learned how to combine Python sets using the `.update()` method.
- I learned how to use a dictionary as a cache for memoization.
- I learned how to use the dictionary `.get()` method when counting values for keys that may not yet exist.
- I became more confident in manually calculating the expected outputs of the algorithms in my project, rather than only understanding their general purpose as I did last week.

## What remains unclear or has been challenging?

### Challenges

- Combining sets in the `annotation()` function was initially difficult. I solved this fairly quickly by searching online for how to combine sets in Python and learned to use the `.update()` method.

- Implementing `information_content()` took more time than the earlier functions. The function receives a dictionary whose keys are genes and whose values are sets of propagated HPO terms, but it needs to produce a new dictionary whose keys are HPO terms and whose values are their Information Content values. To understand and verify the execution of the algorithm, I used the website Python Tutor (`pythontutor.com`).

- In `information_content()`, I also had difficulty understanding why `information_content[term] += 1/N` did not work when the term had not yet been added to the dictionary. By asking the AI tutor on the Python Tutor website, I learned that the problem was that Python cannot increment the value of a dictionary key that does not yet exist. The AI tutor suggested using the dictionary `.get()` method with a default value of `0`, which solved the problem.

### Questions

- Are the current function and variable names descriptive enough according to the code-quality criteria of this course?

- I currently have seven unit tests covering the implemented ontology and annotation-related functionality. Is this a reasonable amount of testing at this stage, or should I already add more tests for these components?

- Should I add comments inside the functions to explain individual stages of the algorithms, or are clear function names and docstrings sufficient at this stage?

- Should implementation choices such as using ancestor-or-self sets in `ancestors()` and annotation propagation, or using a base-2 logarithm in `information_content()`, be documented explicitly somewhere in the project documentation, for example in the implementation document?

- Last week I received a suggestion to include visualization in the project so that the correctness of the results would be easier to inspect and debug. I am still unsure what kind of visualization would be most useful and at what stage it should be implemented. One possibility could be a similarity matrix between patient HPO terms and gene-profile HPO terms. Another possibility could be some form of visualization of the HPO graph itself.

## What will I do next?

- I will write unit tests for `information_content()`.
- I will continue implementing the remaining semantic-similarity components, including MICA, Resnik similarity, BMA, and the Jaccard baseline.
- I will add corresponding unit tests as these components are implemented.

## Time spent

I spent **14 hours and 50 minutes** working on the course this week.
