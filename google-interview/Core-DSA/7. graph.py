# Design Graph
# Design a directed Graph class.

# Your Graph class should support the following operations:

# Graph() will initialize an empty directed graph.
# void addEdge(int src, int dst) will add an edge from src to dst if it does not already exist. If either src or dst do not exist, add them to the graph.
# bool removeEdge(int src, int dst) will remove the edge from src to dst if it exists. Return whether the edge was removed. Either src or dst may not exist in the graph.
# bool hasPath(int src, int dst) will return whether there is a path from src to dst. Assume both src and dst exist in the graph.
# Constraints:

# Each vertex value will be a unique integer.
# Multiple edges from one vertex to another are not allowed.
# A vertex will not have an edge to itself, but the graph may contain a cycle.
# The graph is not necessarily connected (there may be disconnected components).
# Example 1:

# Input:
# ["addEdge", 1, 2, "addEdge", 2, 3, "hasPath", 1, 3, "hasPath", 3, 1, "removeEdge", 1, 2, "hasPath", 1, 3]

# Output:
# [null, null, true, false, true, false]
# Example 2:

# Input:
# ["addEdge", 1, 2, "addEdge", 2, 3, "addEdge", 3, 1, "hasPath", 1, 3, "hasPath", 3, 1]

# Output:
# [null, null, null, true, true]


# Graph Implementation using Adjacency List
from collections import deque

class Graph:
    def __init__(self):
        # Initialize an empty adjacency list to store the graph
        self.adj_list = {}

    def addEdge(self, src: int, dst: int) -> None:
        # Add an edge from source to destination in the graph
        # If source or destination doesn't exist, add them to the graph
        if src not in self.adj_list:
            self.adj_list[src] = set()
        if dst not in self.adj_list:
            self.adj_list[dst] = set()
        # Add the destination as a neighbor of the source
        self.adj_list[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        # Remove an edge from source to destination in the graph
        # Check if source and destination exist in the graph
        if src not in self.adj_list or dst not in self.adj_list[src]:
            return False
        # Remove the destination from the neighbors of the source
        self.adj_list[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        # Check if there is a path from source to destination using DFS
        visited = set()  # Set to keep track of visited nodes
        return self._dfs(src, dst, visited)

    def _dfs(self, src: int, dst: int, visited: set) -> bool:
        # Helper function for DFS traversal
        if src == dst:
            return True  # If source equals destination, path found
        visited.add(src)  # Mark source as visited
        for neighbor in self.adj_list.get(src, []):  # Visit neighbors
            if neighbor not in visited:  # If neighbor is not visited
                if self._dfs(neighbor, dst, visited):  # Recursively check for path
                    return True  # If path found, return True
        return False  # If no path found, return False

    # Alternatively, use BFS for finding paths
    def hasPathBFS(self, src: int, dst: int) -> bool:
        visited = set()  # Set to keep track of visited nodes
        queue = deque([src])  # Initialize queue for BFS traversal
        while queue:
            curr = queue.popleft()  # Get the current node from the queue
            if curr == dst:  # If current node equals destination, path found
                return True
            visited.add(curr)  # Mark current node as visited
            for neighbor in self.adj_list.get(curr, []):  # Visit neighbors
                if neighbor not in visited:  # If neighbor is not visited
                    queue.append(neighbor)  # Add neighbor to queue for traversal
                    visited.add(neighbor)  # Mark neighbor as visited
        return False  # If no path found, return False

