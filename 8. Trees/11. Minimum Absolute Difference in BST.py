# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.diff = float('inf')

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if self.prev is not None:
                self.diff = min(self.diff, abs(root.val - self.prev))
            self.prev = root.val
            dfs(root.right) 
        
        dfs(root)
        return self.diff
