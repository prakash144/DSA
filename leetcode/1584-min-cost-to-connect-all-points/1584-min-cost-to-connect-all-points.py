class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Minimum Spanning Tree : Prim's Algo
        # TC : O(n2logn)
    
        # Create Edges
        manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        N = len(points)

        # Build adjacency list
        adj = {i: [] for i in range(N)}
        for i in range(N):
            for j in range(i+1, N):
                d = manhattan(points[i], points[j])
                adj[i].append((d, j))
                adj[j].append((d, i))

        # Prim's Algorithm
        res = 0
        visited = set()
        minHeap = [(0, 0)]  # List of [cost, node]

        while len(visited) < N:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            res += cost
            for neiCost, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (neiCost, nei))

        return res
        
        
        
        
        
        
        