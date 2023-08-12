import pytest
from scripts.graph import Graph, GraphError

@pytest.fixture
def graph_instance():
    return Graph()

def test_add_vertex(graph_instance):
    vertex = graph_instance.add_vertex('A')
    assert 'A' in graph_instance.get_vertices()
    assert vertex.value == 'A'

def test_add_edge(graph_instance):
    vertex1 = graph_instance.add_vertex('A')
    vertex2 = graph_instance.add_vertex('B')
    graph_instance.add_edge('A', 'B', 5)
    neighbors = graph_instance.get_neighbors('A')
    assert neighbors == [('B', 5)]
    neighbors = graph_instance.get_neighbors('B')
    assert neighbors == [('A', 5)]

def test_get_vertices(graph_instance):
    graph_instance.add_vertex('A')
    graph_instance.add_vertex('B')
    vertices = graph_instance.get_vertices()
    assert vertices == ['A', 'B']

def test_get_neighbors(graph_instance):
    vertex1 = graph_instance.add_vertex('A')
    vertex2 = graph_instance.add_vertex('B')
    graph_instance.add_edge('A', 'B', 5)
    neighbors = graph_instance.get_neighbors('A')
    assert neighbors == [('B', 5)]

def test_size(graph_instance):
    assert graph_instance.size() == 0
    graph_instance.add_vertex('A')
    graph_instance.add_vertex('B')
    assert graph_instance.size() == 2

def test_duplicate_vertex(graph_instance):
    graph_instance.add_vertex('A')
    with pytest.raises(GraphError):
        graph_instance.add_vertex('A')

def test_invalid_edge(graph_instance):
    with pytest.raises(GraphError):
        graph_instance.add_edge('A', 'B', 5)
