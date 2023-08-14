import pytest
from scripts.graphbusiness import business_trip ,Graph


def test_business_trip_valid():
    graph = Graph()
    graph.add_vertex("Metroville")
    graph.add_vertex("Pandora")
    graph.add_edge("Metroville", "Pandora", 82)

    assert business_trip(graph, ["Metroville", "Pandora"]) == 82

def test_business_trip_invalid():
    graph = Graph()
    graph.add_vertex("Metroville")
    graph.add_vertex("Pandora")
    graph.add_edge("Metroville", "Pandora", 82)

    assert business_trip(graph, ["Naboo", "Pandora"]) is None

if __name__ == "__main__":
    pytest.main()
