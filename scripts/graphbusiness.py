class Graph:
    """
    A class representing a graph and its operations.

    Attributes:
        vertices (dict): A dictionary representing the vertices (nodes) and their neighbors.

    Methods:
        add_vertex(vertex): Adds a vertex to the graph.
        add_edge(start_vertex, end_vertex, cost): Adds an edge with a cost between two vertices.
        get_neighbors(vertex): Returns the neighbors of a vertex.
    """

    def __init__(self):
        """
        Initializes an empty graph with no vertices.
        """
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph.

        Args:
            vertex: The vertex to be added.

        Returns:
            None
        """
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, start_vertex, end_vertex, cost):
        """
        Adds an edge with a cost between two vertices.

        Args:
            start_vertex: The starting vertex of the edge.
            end_vertex: The ending vertex of the edge.
            cost: The cost associated with the edge.

        Returns:
            None
        """

        if start_vertex in self.vertices and end_vertex in self.vertices:
            self.vertices[start_vertex].append((end_vertex, cost))

    def get_neighbors(self, vertex):
        """
        Returns the neighbors of a vertex.

        Args:
            vertex: The vertex for which to retrieve neighbors.

        Returns:
            list: A list of tuples representing neighbors and their associated costs.
        """
        return self.vertices.get(vertex, [])

def business_trip(graph, city_names):
    """
    Calculates the total cost of traveling between cities in the given graph.

    Args:
        graph (Graph): The graph containing city connections and costs.
        city_names (list): The list of city names to travel through.

    Returns:
        int or None: The total cost of the trip, or None if the trip is not possible.
    """
    if not graph or not city_names:
        return None

    total_cost = 0

    for i in range(len(city_names) - 1):
        current_city = city_names[i]
        next_city = city_names[i + 1]

        neighbors = graph.get_neighbors(current_city)

        found_edge = None
        for neighbor, cost in neighbors:
            if neighbor == next_city:
                found_edge = (neighbor, cost)
                break

        if found_edge is None:
            return None
        else:
            total_cost += found_edge[1]

    return total_cost

if __name__ == "__main__":
    graph = Graph()

    # Add vertices and edges as needed
    graph.add_vertex("Metroville")
    graph.add_vertex("Pandora")
    graph.add_edge("Metroville", "Pandora", 82)

    graph.add_vertex("Arendelle")
    graph.add_vertex("New Monstropolis")
    graph.add_vertex("Naboo")
    graph.add_vertex("Narnia")
    graph.add_edge("Arendelle", "New Monstropolis", 42)
    graph.add_edge("New Monstropolis", "Naboo", 73)
    graph.add_edge("Naboo", "Narnia", 250)
    graph.add_edge("Naboo", "Metroville", 26)
    graph.add_edge("New Monstropolis", "Metroville", 105)
    graph.add_edge("Arendelle", "Metroville", 99)
    graph.add_edge("Metroville", "Narnia", 37)

    city_names = ["Metroville", "Pandora"]
    cost = business_trip(graph, city_names)
    print("Total cost:", cost)
