class GraphError(Exception):
    pass

class Vertex:
    def __init__(self, value):
        """
        Initialize a vertex with a given value.

        :param value: The value associated with the vertex.
        """
        self.value = value
        self.edges = []

class Graph:
    def __init__(self):
        """
        Initialize an empty graph.
        """
        self.vertices = {}

    def add_vertex(self, value):
        """
        Add a new vertex to the graph.

        :param value: The value associated with the new vertex.
        :return: The newly added vertex.
        :raises GraphError: If a vertex with the same value already exists in the graph.
        """
        if value in self.vertices:
            raise GraphError("Vertex already exists")
        vertex = Vertex(value)
        self.vertices[value] = vertex
        return vertex

    def add_edge(self, vertex1, vertex2, weight=None):
        """
        Add an edge between two vertices in the graph.

        :param vertex1: The value of the first vertex.
        :param vertex2: The value of the second vertex.
        :param weight: (Optional) The weight of the edge.
        :raises GraphError: If either vertex is not present in the graph.
        """
        if vertex1 not in self.vertices or vertex2 not in self.vertices:
            raise GraphError("Both vertices should already be in the graph")
        self.vertices[vertex1].edges.append((vertex2, weight))
        self.vertices[vertex2].edges.append((vertex1, weight))

    def get_vertices(self):
        """
        Get a list of all vertices in the graph.

        :return: A list of vertex values.
        """
        return list(self.vertices.keys())

    def get_neighbors(self, vertex):
        """
        Get the neighbors of a given vertex.

        :param vertex: The value of the vertex.
        :return: A list of neighboring vertices and their  weights.
        :raises GraphError: If the vertex is not present in the graph.
        """
        if vertex not in self.vertices:
            raise GraphError("Vertex not found")
        return self.vertices[vertex].edges

    def size(self):
        """
        Get the number of vertices in the graph.

        :return: The number of vertices.
        """
        return len(self.vertices)
