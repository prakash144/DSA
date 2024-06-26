class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        res = []
        
        def binary_search(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        for num in nums:
            idx = binary_search(sorted_nums, num)
            res.append(idx)
            sorted_nums.pop(idx)  # Remove the element from the sorted array
        return res
                
            
        