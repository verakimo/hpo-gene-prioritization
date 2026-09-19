## Data

The project uses data from the Human Phenotype Ontology (HPO).

Download the following files from the official Human Phenotype Ontology page in OBO Foundry (link: https://obofoundry.org/ontology/hp?utm_source=chatgpt.com):

- `hp.obo` — HPO ontology in OBO format
- `genes_to_phenotype.txt` — HPO gene-to-phenotype annotations

Place both files in the `data/` directory:

    data/
        hp.obo
        genes_to_phenotype.txt

The data files are not included in the repository and are listed in `.gitignore`.

The current development and testing were performed using the HPO release from 2026-09-01.

## Running the program

Run the program from the project root with:

    PYTHONPATH=src poetry run python src/main.py

The program asks for the patient's phenotype terms as Human Phenotype Ontology (HPO) IDs separated by spaces.

Example input:

    HP:0002460 HP:0002451

The program ranks genes according to phenotype-profile semantic similarity and displays the top gene candidates together with their similarity scores, direct HPO annotations, and exact matches with the input phenotype terms.