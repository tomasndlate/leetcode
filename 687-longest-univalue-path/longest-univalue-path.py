# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        longestPath = 0

        def dfs(node, prev):
            nonlocal longestPath
            if not node:
                return 0
            
            itself = node.val == prev # True (1) or False (0)
            left = dfs(node.left, node.val)
            right = dfs(node.right, node.val)

            longestPath = max(longestPath, left + right)

            return 1 + max(left, right) if itself else 0
        
        dfs(root, root.val)
        return longestPath