class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_map = {}
        
        for n in nums:
            count_map[n] = 1 + count_map.get(n,0)
          
        for num, count in count_map.items():
            if count != 3:
                return num
        