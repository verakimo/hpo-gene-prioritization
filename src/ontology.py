toy_parents = {
    "ROOT": set(),
    "A": {"ROOT"},
    "B": {"ROOT"},
    "C": {"A"},
    "D": {"A", "B"}
}

ancestor_cache = {}

def dfs(node, visited):
    """Traverses the graph from the given HPO term to its parents 
    and adds the visited terms to visited.
    
    Args:
        node: The HPO term from which the current DFS step begins.
        visited: A set of HPO terms that have already been visited.
    """
    if node in visited:
        return
    visited.add(node)

    for next_node in toy_parents[node]:
        dfs(next_node, visited)


def ancestors(term):
    """Finds the ancestor-or-self set for a given HPO term.
    Uses cached results when available.

    Args:
        term: The HPO term for which ancestors are being sought.

    Returns:
        A set containing the term itself and all its ancestors.
    """
    if term in ancestor_cache:
        return ancestor_cache[term]
    else:
        visited = set()
        dfs(term, visited)
        ancestor_cache[term] = visited
        return visited
