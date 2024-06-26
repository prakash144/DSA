class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixCount = {0:1}
        
        for n in nums:
            curSum += n
            diff = curSum - k
            res += prefixCount.get(diff, 0)
            prefixCount[curSum] = 1 + prefixCount.get(curSum, 0)
        
        return res

        
        