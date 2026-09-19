"""Provides HPO ontology traversal and ancestor lookup functions."""

class Ontology:
    """Represents an HPO ontology graph and provides ancestor traversal."""
    def __init__(self, parents):
        """Initialize an ontology with a parent mapping.

        Args:
            parents: Mapping from HPO terms to their parent terms.
        """
        self.parents = parents
        self.ancestor_cache = {}


    def dfs(self, node, visited):
        """Traverses the graph from the given HPO term to its parents 
        and adds the visited terms to visited.
        
        Args:
            node: The HPO term from which the current DFS step begins.
            visited: A set of HPO terms that have already been visited.
        """
        if node in visited:
            return
        visited.add(node)

        for next_node in self.parents[node]:
            self.dfs(next_node, visited)


    def ancestors(self, term):
        """Finds the ancestor-or-self set for a given HPO term.
        Uses cached results when available.

        Args:
            term: The HPO term for which ancestors are being sought.

        Returns:
            A set containing the term itself and all its ancestors.
        """
        if term in self.ancestor_cache:
            return self.ancestor_cache[term]
        visited = set()
        self.dfs(term, visited)
        self.ancestor_cache[term] = visited
        return visited
