class Graph:
    """
    A class representing a graph and its operations.

    Attributes:
        graph (dict): A dictionary representing the graph's nodes and their neighbors.

    Methods:
        add_edge(node, neighbor): Adds an edge between a node and its neighbor.
        depth_first(start_node): Performs a depth-first traversal starting from the given node.
    """

    def __init__(self):
        """
        Initializes an empty graph.
        """
        self.graph = {}

    def add_edge(self, node, neighbor):
        """
        Adds an edge between a node and its neighbor.

        Args:
            node: The node to which the neighbor will be added.
            neighbor: The neighbor node to be added.

        Returns:
            None
        """
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def depth_first(self, start_node):
        """
        Performs a depth-first traversal starting from the given node.

        Args:
            start_node: The starting node for the depth-first traversal.

        Returns:
            list: A list containing the nodes visited during the depth-first traversal.
        """
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
