toy_parents = {
    "ROOT": set(),
    "A": {"ROOT"},
    "B": {"ROOT"},
    "C": {"A"},
    "D": {"A", "B"}
}

def dfs(node, visited):
    """Traverses the graph from the given HPO term to its parents 
    and adds the visited terms to visited.
    
    Args:
        node: The HPO term from which the current DFS step begins.
        visited: A set of HPO terms that have already been visited.

    Returns:
        Not needed.
    """
    if node in visited:
        return
    visited.add(node)

    for next_node in toy_parents[node]:
        dfs(next_node, visited)


def ancestors(term):
    """Finds the ancestor-or-self set for a given HPO term.

    Args:
        term: The HPO term for which ancestors are being sought.

    Returns:
        A set containing the term itself and all its ancestors.
    """
    visited = set()
    dfs(term, visited)
    return visited
