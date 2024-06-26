# Prim's Algorithm
# Implement Prim's minimum spanning tree algorithm.

# A Minimum Spanning Tree (MST) is a tree that spans all the vertices in a given weighted, undirected graph while minimizing the total edge weight and avoiding cycles. It connects all nodes with exactly
# ∣V∣−1 edges, where V is the set of vertices, and has the lowest possible sum of edge weights.

# Prim's algorithm is a greedy algorithm that builds the MST of a graph starting from an arbitrary vertex. At each step, the algorithm adds the lightest edge connecting a vertex in the MST to a vertex outside the MST, effectively "growing" the MST one edge at a time.

# Objective:

# Given a weighted, undirected graph, find the minimum spanning tree (MST) using Prim's algorithm and return its total weight. If the graph is not connected, the total weight of the minimum spanning tree should be -1.

# Input:

# n - the number of vertices in the graph, where (2 <= n <= 100). Each vertex is labeled from 0 to n - 1.
# edges - a list of tuples, each representing an undirected edge in the form (u, v, w), where u and v are vertices connected by the edge, and w is the weight of the edge, where (1 <= w <= 10).

# Example 1:
    
# Input:
# n = 5
# edges = [[0,1,10], [0,2,3], [1,3,2], [2,1,4], [2,3,8], [2,4,2], [3,4,5]]

# Output:
# 11

from typing import List
import heapq

class Solution:
    # Implementation for Prim's algorithm to compute Minimum Spanning Trees
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # Build the adjacency list
        adj = {}
        for i in range(n):
            adj[i] = []
        # Add edges to the adjacency list
        for n1, n2, weight in edges:
            adj[n1].append([n2, weight])
            adj[n2].append([n1, weight])

        minHeap = [[0,0]]  # Heap to store vertices with their weights, start BFS at vertex 0
        res = 0  # Total weight of the Minimum Spanning Tree (MST)
        visit = set()  # Set to keep track of visited vertices
        while minHeap and len(visit) < n:
            weight, v = heapq.heappop(minHeap)  # Pop the vertex with the minimum weight
            if v in visit:
                continue  # Skip if already visited

            res += weight  # Add the weight to the MST
            visit.add(v)   # Mark vertex as visited
            # Explore neighbors of the current vertex and update the heap
            for neighbor, weight in adj[v]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, [weight, neighbor])  # Add neighbor to the heap

        # Return -1 if not all nodes are visited (indicating an unconnected graph)
        return res if len(visit) == n else -1 


