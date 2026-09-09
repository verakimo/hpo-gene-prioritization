toy_parents = {
    "ROOT": set(),
    "A": {"ROOT"},
    "B": {"ROOT"},
    "C": {"A"},
    "D": {"A", "B"}
}

class ontology:

    def dfs(node, visited):
        if node in visited:
            return
        visited.add(node)

        for next_node in toy_parents[node]:
            dfs(next_node, visited)

    def ancestors(term):
        visited = set()
        dfs(term, visited)
        return visited
