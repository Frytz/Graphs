"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()
        
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.vertices or v2 not in self.vertices:
            print("attempting to add edge to non-existing node")
            return 
       
        self.vertices[v1].add(v2)
      

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]
       
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        visited = set()

        queue.enqueue(starting_vertex)
        while queue.size() > 0:
            vertex = queue.dequeue()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for next_vertex in self.vertices[vertex]:
                    queue.enqueue(next_vertex)
    

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()

        stack.push(starting_vertex)
        while stack.size() > 0:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for next_vertex in self.vertices[vertex]:
                    stack.push(next_vertex)
#  
    def dft_recursive(self, starting_vertex, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # visited = set()
        if starting_vertex not in visited:
           
            print(starting_vertex)
            visited.add(starting_vertex)
            neighbors = self.get_neighbors(starting_vertex)
            for node in neighbors:
                self.dft_recursive(node)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        if starting_vertex == destination_vertex:
            return [starting_vertex]

        else:

            #will contain complete paths
            queue = Queue()
            queue.enqueue([starting_vertex])

            visited = set()


        while queue:

            path = queue.dequeue()
            last_vertex = path[-1]

            adjacent_vertices = self.vertices[last_vertex]

            # cycle through all non visited adjacent vertices
            for vertex in adjacent_vertices:
                if vertex not in visited:
                    new_path = path.copy()
                    new_path.append(vertex)
                    if vertex == destination_vertex:
                        return new_path
                    else:
                        queue.enqueue(new_path)
            visited.add(last_vertex)
            
            
        return []


    def dfs(self, starting_vertex, destination_vertex, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        if visited == None:
            visited = set()

        start_path = [starting_vertex]

        if starting_vertex == destination_vertex:
            return [starting_vertex]

        else:
            # Flag current vertex as visited
            visited.add(starting_vertex)

            # get set of adjacent vertices
            adjacent_vertices = self.vertices[starting_vertex]

            # get adjacent vertices not already visited
            adjacent_not_visited = adjacent_vertices.difference(visited)

            #process adjacent vertices not already visited
            for vertex in adjacent_not_visited:
                found = self.dfs(vertex, destination_vertex, visited)
                if found:
                    return start_path + found
            return None

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        if starting_vertex == destination_vertex:
            return [destination_vertex]

        if starting_vertex not in visited: 
            visited.add(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                path = self.dfs_recursive(neighbor, destination_vertex, visited)
                if path:
                    return [starting_vertex] + path

        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
