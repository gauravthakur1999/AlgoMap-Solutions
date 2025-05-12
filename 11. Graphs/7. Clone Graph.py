"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Approach:
        - Use DFS to traverse and clone the graph.
        - Use a dictionary to map original nodes to their cloned copies.
        """

        if not node:
            return None

        visited = {}

        def dfs(curr):
            # If already cloned, return the copy
            if curr in visited:
                return visited[curr]

            # Create a new copy of the node
            clone = Node(curr.val)
            visited[curr] = clone

            # Recursively clone neighbors
            for neighbor in curr.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)