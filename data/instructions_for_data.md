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