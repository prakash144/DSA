class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Prioprity Queue or minHeap, retrieval - O(logn)
        # TC - O(ElogV)
        edges = collections.defaultdict(list)
        time = {}
        
        for u, v, w in times:
            edges[u].append((v, w))
        
        minHeap = [(0, k)]
        
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in time:
                continue
            time[n1] = w1
            
            for n2, w2 in edges[n1]:
                if n2 not in time:
                    heapq.heappush(minHeap, (w1 + w2, n2))
                    
        return max(time.values()) if len(time) == n else -1
                    
        