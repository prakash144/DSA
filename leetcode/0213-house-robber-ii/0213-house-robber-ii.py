class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.rob_I(nums[1:]), self.rob_I(nums[:-1]))
    
    def rob_I(self, num):
        rob_1, rob_2 = 0, 0

        for n in num:
            temp = max(rob_1+n, rob_2)
            rob_1 = rob_2
            rob_2 = temp

        return rob_2