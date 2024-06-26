# Matrix Breadth-First Search
# You are given a binary matrix Grid where 0s represent land and 1s represent rocks that can not be traversed.

# Return the length of the shortest path from the top-left corner of Grid to the bottom-right corner such that all traversed cells are land cells. You may only move vertically or horizontally through land cells.

# Note:

# If there is no such path, return -1.
# The length of a path is the number of moves from the starting cell to the ending cell.
# Example 1:

# Input: grid = [
#   [0, 0, 0, 0],
#   [1, 1, 0, 0],
#   [0, 0, 0, 1],
#   [0, 1, 0, 0]
# ]

# Output:
# 6

from collections import deque
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns in the grid
        ROWS, COLS = len(grid), len(grid[0])
        
        # Set to keep track of visited cells
        visit = set()
        
        # Queue for BFS traversal
        queue = deque()
        
        # Start BFS from the top-left cell
        queue.append((0, 0))
        
        # Mark the starting cell as visited
        visit.add((0, 0))

        # Initialize length of the shortest path
        length = 0
        
        # While there are cells to explore
        while queue:
            # Process each cell at the current level separately
            for i in range(len(queue)):
                # Get the current cell
                r, c = queue.popleft()
                
                # If reached the destination, return the length of the shortest path
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                # Define neighbors: right, left, down, up
                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                
                # Explore each neighbor
                for dr, dc in neighbors:
                    # Calculate the coordinates of the neighbor
                    nr, nc = r + dr, c + dc
                    
                    # Check if neighbor is out of bounds or visited or obstacle
                    if (min(nr, nc) < 0 or nr == ROWS or nc == COLS or
                        (nr, nc) in visit or grid[nr][nc] == 1):
                        continue
                    
                    # Add the valid neighbor to the queue and mark it as visited
                    queue.append((nr, nc))
                    visit.add((nr, nc))
            # Increment the length for each level in BFS
            length += 1
        
        # If destination is unreachable, return -1
        return -1
