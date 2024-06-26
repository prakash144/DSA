class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize a result list with all elements set to 1
        res = [1] * len(nums)
        
        # Step 1: Calculate the prefix products
        prefix = 1
        for i in range(len(nums)):
            # Store the product of all elements before the current index
            res[i] = prefix
            # Update the prefix product by multiplying with the current element
            prefix *= nums[i]
            
        # Step 2: Calculate the postfix products and update the result list
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            # Multiply the postfix product with the current element and update the result list
            res[i] *= postfix
            # Update the postfix product by multiplying with the current element
            postfix *= nums[i]
            
        return res
