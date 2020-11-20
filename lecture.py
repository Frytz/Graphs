

class Graph:

    def __init__(self):
        self.verticies = {}

    def __repr__ (self):
        return str(self.verticies)

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.verticies[vertex_id] = set()
    def remove_vertex(self, vertex_id):
        if vertex_id not in self.verticies:
            return
        self.verticies.pop(vertex_id)
        for remaining_vertex in self.verticies:
            self.verticies[remaining_vertex].discard(vertex_id)

    def add_edge(self, from_vertex_id, to_vertex_id):
        """
        Add a directed edge to the graph.
        """
        if from_vertex_id not in self.verticies or to_vertex_id not in self.verticies:
            print("attempting to add edge to non-existing node")
            return 
       
        self.verticies[from_vertex_id].add(to_vertex_id)
    
    def remove_edge(self, from_vertex_id, to_vertex_id):
        if from_vertex_id not in self.verticies or to_vertex_id not in self.verticies:
            return
        self.verticies[from_vertex_id].discard(to_vertex_id)
        
      

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.

        """
        return self.verticies[vertex_id]
       

graph = Graph()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
# print(graph)
graph.add_edge(1,2)
graph.add_edge(2,3)
graph.add_edge(3,4)
graph.add_edge(4,1)
# print(graph)
# print(graph.get_neighbors(1))
# print(graph.get_neighbors(4))
# print(graph)
graph.remove_vertex(4)
print(graph)
# graph.remove_edge(4,1)
# print(graph)