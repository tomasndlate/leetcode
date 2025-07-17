# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lowest = None

        def dfs(node):
            nonlocal lowest
            if not node:
                return False
            
            left = dfs(node.left)
            right = dfs(node.right)
            itself = node == p or node == q

            # at least 2 flags positive (True = 1, False = 0)
            if left + right + itself >= 2:
                lowest = node

            return left or right or itself

        dfs(root)
        return lowest