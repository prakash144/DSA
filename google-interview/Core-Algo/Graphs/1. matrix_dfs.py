# Matrix Depth-First Search
# You are given a binary matrix Grid where 0s represent land and 1s represent rocks that can not be traversed.

# Return the number of unique paths from the top-left corner of Grid to the 
# bottom-right corner such that all traversed cells are land cells. 
# You may only move vertically or horizontally through land cells. 
# For an individual unique path you cannot visit the same cell twice.

# Example 1:

# Input: grid = [
#   [0, 0, 0, 0],
#   [1, 1, 0, 0],
#   [0, 0, 0, 1],
#   [0, 1, 0, 0]
# ]

# Output:
# 2

from typing import List

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns in the grid
        ROWS, COLS = len(grid), len(grid[0])

        def helper(grid: List[List[int]], r: int, c: int, visit: set) -> int:
            # Check if current cell is out of bounds, visited, or obstacle
            if (min(r, c) < 0 or
                r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] == 1):
                return 0
            
            # If reached the destination, return 1
            if r == ROWS - 1 and c == COLS - 1:
                return 1

            # Mark current cell as visited
            visit.add((r, c))

            # Initialize count for paths from current cell
            count = 0
            
            # Explore neighbors: down, up, right, left
            count += helper(grid, r + 1, c, visit)  # Down
            count += helper(grid, r - 1, c, visit)  # Up
            count += helper(grid, r, c + 1, visit)  # Right
            count += helper(grid, r, c - 1, visit)  # Left

            # Unmark current cell as visited for backtracking
            visit.remove((r, c))
            
            # Return the total count of paths from current cell
            return count

        # Start DFS from the top-left cell and return the count of paths
        return helper(grid, 0, 0, set())
