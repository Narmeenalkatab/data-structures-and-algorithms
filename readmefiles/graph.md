# CC-35: Graph


## Problem Domain: Graph Implementation

 Implementing a graph data structure and associated methods.

### Approach

1. **Graph Implementation:**
   - Create a class named `Graph` to represent the graph using an adjacency list.
   - Initialize the graph's data structure (dictionary) to store vertices as keys and their edges as values (a list of tuples).
   - Implement methods for adding vertices, adding edges, retrieving vertices, getting neighbors, and calculating size.

2. **Add Vertex:**
   - Create a method `add_vertex(value)` that takes a vertex value and adds it to the graph as a key in the vertices dictionary.

3. **Add Edge:**
   - Create a method `add_edge(vertex1, vertex2, weight=None)` that connects two vertices with an edge.
   - Check if both `vertex1` and `vertex2` exist in the vertices dictionary. If not, raise a custom `GraphError`.
   - Append a tuple `(vertex2, weight)` to the list of edges for `vertex1`, and vice versa.

4. **Get Vertices:**
   - Create a method `get_vertices()` that returns a list of all vertices in the graph by extracting keys from the vertices dictionary.

5. **Get Neighbors:**
   - Create a method `get_neighbors(vertex)` that takes a vertex and returns its neighbors along with their weights.
   - Check if the given `vertex` exists in the vertices dictionary. If not, raise a custom `GraphError`.
   - Return the list of edges associated with the given vertex.

6. **Size:**
   - Create a method `size()` that returns the count of vertices in the graph by calculating the length of the vertices dictionary.

7. **Custom Exception:**
   - Define a custom exception class named `GraphError` to capture errors specific to the graph operations.

### Big O Notation

#### Time Complexities:

- **Add Vertex:** O(1)
- **Add Edge:** O(1)
- **Get Vertices:** O(V)
- **Get Neighbors:** O(E)
- **Size:** O(1)

#### Space Complexities:

- **Add Vertex:** O(1)
- **Add Edge:** O(1)
- **Get Vertices:** O(V)
- **Get Neighbors:** O(E)
- **Size:** O(1)

The complexities are based on the number of vertices (V) and edges (E) in the graph.




# Run in terminal

__pytest tests/test_graph.py__

# Implementation Code and Test
[Code](../scripts/graph.py)

[Test](../tests/test_graph.py)