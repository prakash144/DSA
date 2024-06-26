class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Binary Search
        l, r = max(nums), sum(nums)
        res =r
        
        def canSplit(largest):
            subArray = 0
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largest:
                    subArray += 1
                    curSum = n
            return subArray + 1 <=k
                    
        while l <= r:
            m = l + ((r-l)//2)
            if canSplit(m):
                res = m
                r = m - 1
            else:
                l = m +1
                
        return res
                