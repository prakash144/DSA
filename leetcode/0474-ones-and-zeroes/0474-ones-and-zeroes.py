class Solution:
    def findMaxForm(self, strs: List[str], M: int, N: int) -> int:
        dp = defaultdict(int)
        for s in strs:
            mCnt, nCnt = s.count("0"), s.count("1")
            for m in range(M, mCnt - 1, -1):
                for n in range(N, nCnt - 1, -1):
                    dp[(m, n)] = max(
                        1 + dp[(m - mCnt, n - nCnt)],
                        dp[(m, n)])
        return dp[(M, N)]
                
        