"""Provides functions for parsing HPO ontology data from OBO files."""

def parse_obo(file_path):
    """Parse HPO parent relationships from an OBO file.

    Args:
        file_path: Path to the HPO OBO file.

    Returns:
        A dictionary mapping each HPO term to a set of its parent terms.
    """
    parents = {}
    with open(file_path, encoding="utf-8") as hpo_dag:
        for line in hpo_dag:
            if line.startswith("id:"):
                node = line.split()[1]
                parents[node] = set()
            if line.startswith("is_a"):
                parents[node].add(line.split()[1])
            if line.startswith("[Typedef]"):
                break
    return parents
