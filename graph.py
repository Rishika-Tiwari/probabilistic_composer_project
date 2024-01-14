import random

class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent = {}  # nodes that it points to
        self.neighbors = []
        self.neighbors_weights = []

    def __str__(self):
        return f"{self.value} {' '.join(node.value for node in self.adjacent.keys())}"

    def add_edge_to(self, vertex, weight=0):
        # adding an edge to the vertex we input with weight
        self.adjacent[vertex] = weight
        self.neighbors.append(vertex)
        self.neighbors_weights.append(weight)

    def increment_edge(self, vertex):
        # incrementing the weight of an edge
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_adjacent_nodes(self):
        return set(self.adjacent.keys())

    def get_probability_map(self):
        for vertex, weight in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)

    def next_word(self):
        # randomly select the next word based on weights
        return random.choices(self.neighbors, weights=self.neighbors_weights)[0]

class Graph:
    def __init__(self):
        self.vertices = {}

    def get_vertex_values(self):
        # return all possible words (values of all vertices)
        return set(self.vertices.keys())

    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value):
        if value not in self.vertices:
            self.add_vertex(value)
        # get the vertex object
        return self.vertices[value]

    def get_next_word(self, current_vertex):
        return current_vertex.next_word()

    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()

