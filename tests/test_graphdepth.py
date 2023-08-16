import pytest
from scripts.graphdepth import Graph

def test_depth_first_basic():
    graph = Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'G')
    graph.add_edge('C', 'D')
    graph.add_edge('C', 'E')
    graph.add_edge('E', 'H')
    graph.add_edge('D', 'F')

    result = graph.depth_first('A')
    assert result == ['A', 'B', 'G', 'C', 'D', 'F', 'E', 'H']

def test_depth_first_different_start():
    graph = Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'G')
    graph.add_edge('C', 'D')
    graph.add_edge('C', 'E')
    graph.add_edge('E', 'H')
    graph.add_edge('D', 'F')

    result = graph.depth_first('C')
    expected_result = ['C', 'D', 'F', 'E', 'H']
    assert result == expected_result


if __name__ == '__main__':
    pytest.main()
