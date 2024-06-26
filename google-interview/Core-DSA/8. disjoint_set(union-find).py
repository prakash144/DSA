# Design Disjoint Set (Union-Find)
# Design a Disjoint Set (aka Union-Find) class.

# Your UnionFind class should support the following operations:

# UnionFind(int n) will initialize a disjoint set of size n.
# int find(int x) will return the root of the component that x belongs to.
# bool isSameComponent(int x, int y) will return whether x and y belong to the same component.
# bool union(int x, int y) will union the components that x and y belong to. If they are already in the same component, return false, otherwise return true.
# int getNumComponents() will return the number of components in the disjoint set.
# Example 1:

# Input:
# ["UnionFind", 10, "isSameComponent", 1, 3, "union", 1, 2, "union", 2, 3, "getNumComponents", "isSameComponent", 1, 3]

# Output:
# [null, 1, false, true, true, 8, true]
# Note: The find method will not be directly tested, but you will need to use it in the implementation of the other methods. Thus, it will be tested indirectly.

class UnionFind:
    def __init__(self, n: int):
        # Initialize the Union-Find data structure with n elements
        self.parent = [i for i in range(n)]  # Initialize each element as its own parent
        self.size = [1] * n  # Initialize size of each component as 1
        self.num_components = n  # Initially, there are n components

    def find(self, x: int) -> int:
        # Finds the root of the component containing element x
        if x != self.parent[x]:
            # If x is not the root, recursively find the root and update the parent pointer
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]  # Return the root of the component

    def isSameComponent(self, x: int, y: int) -> bool:
        # Checks if elements x and y belong to the same component
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        # Connects elements x and y by union operation
        root_x = self.find(x)  # Find the root of x
        root_y = self.find(y)  # Find the root of y
        if root_x != root_y:
            # If x and y are in different components, merge them
            if self.size[root_x] < self.size[root_y]:
                # Attach smaller component to the larger one to maintain balance
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            else:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
            self.num_components -= 1  # Decrement the number of components
            return True  # Return True to indicate successful union
        return False  # Return False if x and y are already in the same component

    def getNumComponents(self) -> int:
        # Returns the number of components in the Union-Find data structure
        return self.num_components

