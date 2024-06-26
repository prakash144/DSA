# Topological Sort
# Implement topological sort.

# Topological sort is an algorithm for linearly ordering the vertices of a directed acyclic graph such that for every directed edge 
# (u,v), vertex u comes before  v in the ordering.

# Given a directed graph, perform a topological sort on its vertices and return the order as a list of vertex labels. There may be multiple valid topological sorts for a given graph, so you may return any valid ordering.

# If the graph contains a cycle, you should return an empty list to indicate that a topological sort is not possible.

# Input:

# n - the number of vertices in the graph. Each vertex is labeled from 0 to n - 1.
# edges - a list of pairs, each representing a directed edge in the form (u, v), where u is the source vertex and v is the destination vertex.
# Example 1:

# Input:
# n = 6
# edges = [[2,3], [3,1], [4,0], [4,1], [5,0], [5,2]]

# Output:
# [5, 4, 2, 3, 1, 0]
# Example 2:

# Input:
# n = 3
# edges = [[0,1], [1,2], [2,0]]

# Output:
# []

from typing import List
from collections import defaultdict

class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        # Create an adjacency list to represent the graph
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)

        topSort = []  # List to store the topological ordering
        visited = set()   # Set to store visited nodes
        visiting = set()  # Set to store nodes being visited in the current DFS call (detect cycles)

        # Depth-First Search (DFS) function to traverse the graph and perform topological sorting
        def dfs(src: int) -> bool:
            if src in visited:
                return True  # Node already visited, no need to visit again
            if src in visiting:
                return False  # A cycle is detected, cannot perform topological sort

            visiting.add(src)  # Mark the node as currently visiting
            
            # Explore neighbors of the current node
            for neighbor in adj[src]:
                if not dfs(neighbor):
                    return False  # A cycle is detected
                
            visiting.remove(src)  # Finished visiting the node
            visited.add(src)     # Mark the node as visited
            topSort.append(src)  # Add the node to the topological ordering
            
            return True  # No cycle detected, continue topological sorting

        # Perform DFS for each node in the graph
        for i in range(n):
            if not dfs(i):
                return []  # Return an empty list if a cycle is detected

        # Reverse the topological ordering to get the correct order
        topSort.reverse()
        return topSort  # Return the topological ordering
