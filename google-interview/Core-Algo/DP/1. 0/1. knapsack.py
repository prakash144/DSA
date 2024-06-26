# 0 / 1 Knapsack
# Solve the 0 / 1 Knapsack problem.

# You are given a list of items, each with a weight and a profit, along with a backpack with a specified maximum capacity. 
# Your goal is to calculate the maximum profit you can achieve without exceeding the backpack's capacity. You must select items such that the total weight of the items is less than or equal to the backpack's capacity. You can select at most one of each item.

# Input:

# profit - a list of n integers, where profit[i] represents the profit of the i-th item. (1 <= profit[i] <= 100)
# weight - a list of n integers, where weight[i] represents the weight of the i-th item. (1 <= weight[i] <= 100)
# capacity - an integer representing the maximum weight the backpack can hold. (1 <= capacity <= 100)
# Here, n is the number of items, where 1 <= n <= 100. You can assume that weight and profit are both the same length and only contain positive integers.
# Example 1:

# Input:
# profit = [4, 4, 7, 1]
# weight = [5, 2, 3, 1]
# capacity = 8

# Output:
# 12
# The maximum profit you can achieve is 12, by selecting the items at index 1, 2 and 3. The total profit is 4 + 7 + 1 = 12, and the total weight is 2 + 3 + 1 = 6, which is less than the backpack's capacity of 8.

from typing import List

class Solution:
    """
    Brute force solution for the 0/1 Knapsack problem.
    Time complexity: O(2^n), Space complexity: O(n)
    """
    def maximumProfitBruteForce(self, profit: List[int], weight: List[int], capacity: int) -> int:
        return self.dfsHelper(0, profit, weight, capacity)

    def dfsHelper(self, i, profit, weight, capacity):
        if i == len(profit):
            return 0

        # Skip item i
        maxProfit = self.dfsHelper(i + 1, profit, weight, capacity)

        # Include item i
        newCap = capacity - weight[i]
        if newCap >= 0:
            p = profit[i] + self.dfsHelper(i + 1, profit, weight, newCap)
            # Compute the max
            maxProfit = max(maxProfit, p)

        return maxProfit


    """
    Memoization solution for the 0/1 Knapsack problem.
    Time complexity: O(n * m), Space complexity: O(n * m)
    """
    def maximumProfitMemoization(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # A 2D array with N rows and M + 1 columns, initialized with -1's
        N, M = len(profit), capacity
        cache = [[-1] * (M + 1) for _ in range(N)]
        return self.memoHelper(0, profit, weight, capacity, cache)

    def memoHelper(self, i, profit, weight, capacity, cache):
        if i == len(profit):
            return 0
        if cache[i][capacity] != -1:
            return cache[i][capacity]

        # Skip item i
        cache[i][capacity] = self.memoHelper(i + 1, profit, weight, capacity, cache)
        
        # Include item i
        newCap = capacity - weight[i]
        if newCap >= 0:
            p = profit[i] + self.memoHelper(i + 1, profit, weight, newCap, cache)
            # Compute the max
            cache[i][capacity] = max(cache[i][capacity], p)

        return cache[i][capacity]


    """
    Dynamic programming solution for the 0/1 Knapsack problem.
    Time complexity: O(n * m), Space complexity: O(n * m)
    """
    def maximumProfitDP(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        dp = [[0] * (M + 1) for _ in range(N)]

        # Fill the first column and row to reduce edge cases
        for i in range(N):
            dp[i][0] = 0
        for c in range(M + 1):
            if weight[0] <= c:
                dp[0][c] = profit[0] 

        for i in range(1, N):
            for c in range(1, M + 1):
                skip = dp[i-1][c]
                include = 0
                if c - weight[i] >= 0:
                    include = profit[i] + dp[i-1][c - weight[i]]
                dp[i][c] = max(include, skip)
        return dp[N-1][M]


    """
    Memory optimized dynamic programming solution for the 0/1 Knapsack problem.
    Time complexity: O(n * m), Space complexity: O(m)
    """
    def maximumProfitMemoryOptimizedDP(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        dp = [0] * (M + 1)

        # Fill the first row to reduce edge cases
        for c in range(M + 1):
            if weight[0] <= c:
                dp[c] = profit[0] 

        for i in range(1, N):
            curRow = [0] * (M + 1)
            for c in range(1, M + 1):
                skip = dp[c]
                include = 0
                if c - weight[i] >= 0:
                    include = profit[i] + dp[c - weight[i]]
                curRow[c] = max(include, skip)
            dp = curRow
        return dp[M]

