class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def depth_first(self, start_node):
        visited = set()
        result = []

        def dfs(node):
            visited.add(node)
            result.append(node)

            if node in self.graph:
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        dfs(neighbor)

        dfs(start_node)
        return result
