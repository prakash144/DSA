class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # delta = n-1 + 0 = n-1
        delta = defaultdict(int)

        for src, dst in trust:
            delta[dst] += 1
            delta[src] -= 1
            
        for i in range(1, n+1):
            if delta[i] == n-1:
                return i
            
        return -1