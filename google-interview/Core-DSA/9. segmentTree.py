# Design Segment Tree
# Design a Segment Tree class.

# Your SegmentTree class should support the following operations:

# SegmentTree(int[] arr) will initialize a segment tree based on the given array arr. You can assume that the array arr is non-empty.
# int query(int l, int r) will return the sum of all elements in the range [l, r] inclusive. You can assume that 0 <= l <= r < arr.length.
# void update(int idx, int val) will update the element at index idx in the original array to be val. You can assume that 0 <= idx < arr.length.
# Example 1:

# Input:
# ["SegmentTree", [1, 2, 3, 4, 5], "query", 0, 2, "query", 2, 4, "update", 3, 0, "query", 2, 4]

# Output:
# [null, 6, 12, null, 8]
# Example 2:

# Input:
# ["SegmentTree", [-1, 2, 4], "query", 0, 1, "query", 1, 2, "update", 2, 3, "query", 0, 2]

# Output:
# [null, 1, 6, null, 4]

class Node:
    def __init__(self, total: int, L: int, R: int):
        # Constructor for a node in the segment tree
        self.sum = total  # Total sum of the range covered by this node
        self.left = None  # Pointer to the left child node
        self.right = None  # Pointer to the right child node
        self.L = L  # Left index of the range covered by this node
        self.R = R  # Right index of the range covered by this node

class SegmentTree:
    def __init__(self, nums):
        # Constructor for the segment tree
        self.root = self.build(nums, 0, len(nums) - 1)  # Build the segment tree
    
    def build(self, nums, L, R):
        # Recursively build the segment tree
        if L == R:
            return Node(nums[L], L, R)  # If single element, create a leaf node
        
        M = (L + R) // 2  # Calculate the middle index
        root = Node(0, L, R)  # Create a new node with initial sum 0
        root.left = self.build(nums, L, M)  # Build left subtree
        root.right = self.build(nums, M + 1, R)  # Build right subtree
        root.sum = root.left.sum + root.right.sum  # Update sum for the current node
        return root
    
    def update(self, index, val):
        # Update the value of an element at the given index
        self.update_helper(self.root, index, val)
    
    def update_helper(self, root, index, val):
        # Helper function to update the value recursively
        if root.L == root.R:
            root.sum = val  # If reached the leaf node, update its sum
            return
        
        M = (root.L + root.R) // 2  # Calculate the middle index
        if index > M:
            self.update_helper(root.right, index, val)  # Update right subtree
        else:
            self.update_helper(root.left, index, val)  # Update left subtree
        root.sum = root.left.sum + root.right.sum  # Update sum for the current node
    
    def query(self, L, R):
        # Query the sum of elements in the given range [L, R]
        return self.query_helper(self.root, L, R)

    def query_helper(self, root, L, R):
        # Helper function to perform range sum query recursively
        if L <= root.L and root.R <= R:
            return root.sum  # If the current node's range is fully covered, return its sum
        
        if R < root.L or L > root.R:
            return 0  # If the current node's range is completely outside the query range, return 0
        
        # Otherwise, recursively query both left and right subtrees
        return self.query_helper(root.left, L, R) + self.query_helper(root.right, L, R)
