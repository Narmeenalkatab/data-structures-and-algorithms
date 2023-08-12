class GraphError(Exception):
    pass

class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = []

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        if value in self.vertices:
            raise GraphError("Vertex already exists")
        vertex = Vertex(value)
        self.vertices[value] = vertex
        return vertex

    def add_edge(self, vertex1, vertex2, weight=None):
        if vertex1 not in self.vertices or vertex2 not in self.vertices:
            raise GraphError("Both vertices should already be in the graph")
        self.vertices[vertex1].edges.append((vertex2, weight))
        self.vertices[vertex2].edges.append((vertex1, weight))

    def get_vertices(self):
        return list(self.vertices.keys())

    def get_neighbors(self, vertex):
        if vertex not in self.vertices:
            raise GraphError("Vertex not found")
        return self.vertices[vertex].edges

    def size(self):
        return len(self.vertices)
