# Kruskal's Algorithm
# Implement Kruskal's minimum spanning tree algorithm.

# A Minimum Spanning Tree (MST) is a tree that spans all the vertices in a given weighted, undirected graph while minimizing the total edge weight and avoiding cycles. It connects all nodes with exactly 
# ∣V∣−1 edges, where V is the set of vertices, and has the lowest possible sum of edge weights.

# Kruskal's algorithm is a greedy algorithm that finds the MST of graph. It sorts all the edges from least weight to greatest, and iteratively adds edges to the MST, ensuring that each new edge doesn't form a cycle.

# Objective:

# Given a weighted, undirected graph, find the minimum spanning tree (MST) using Kruskal's algorithm and return its total weight. If the graph is not connected, the total weight of the minimum spanning tree should be -1.

# Input:

# n - the number of vertices in the graph, where (2 <= n <= 100). Each vertex is labeled from 0 to n - 1.
# edges - a list of tuples, each representing an undirected edge in the form (u, v, w), where u and v are vertices connected by the edge, and w is the weight of the edge, where (1 <= w <= 10).
# Note: If the graph is not connected, you should return -1.

# Example 1:

# Input:
# n = 5
# edges = [[0,1,10], [0,2,3], [1,3,2], [2,1,4], [2,3,8], [2,4,2], [3,4,5]]

# Output:
# 11

import heapq
from typing import List

class UnionFind:
    def __init__(self, n: int):
        # Initialize the parent and size arrays for Union Find
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x: int) -> int:
        # Finds the root of x using path compression
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        # Connects x and y using Union Find
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            else:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
            return True
        return False

class Solution:
    # Implementation for Kruskal's algorithm to compute Minimum Spanning Trees
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # Use a min heap to sort the edges based on their weights
        minHeap = []
        for n1, n2, weight in edges:
            heapq.heappush(minHeap, [weight, n1, n2])

        # Initialize Union Find to keep track of connected components
        unionFind = UnionFind(n)
        res, components = 0, n

        # Pop edges from the min heap and connect nodes until only one component remains
        while components > 1 and minHeap:
            weight, n1, n2 = heapq.heappop(minHeap)
            if unionFind.union(n1, n2):
                res += weight  # Add edge weight to the total weight of MST
                components -= 1  # Decrement the number of components

        # Return -1 if not all nodes are visited (indicating an unconnected graph)
        return res if components == 1 else -1
