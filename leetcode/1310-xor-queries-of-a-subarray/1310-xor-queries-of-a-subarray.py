class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        B = list(itertools.accumulate(arr, func = operator.xor)) + [0]
        return [B[L-1]^B[R] for L,R in queries]
                
                
        