class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = [[]]
        
        for n in nums:
            nextPerm = []
            for p in perm:
                for i in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(i,n)
                    nextPerm.append(pCopy)
                perm = nextPerm
                
        return perm