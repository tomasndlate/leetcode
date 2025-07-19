# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.res = None

        def dfs(node):
            if not node:
                return False

            itself = node == p or node == q
            left = dfs(node.left)
            right = dfs(node.right)

            # if is lowest (2 need to be true)
            if itself + left + right >= 2:
                self.res = node
            
            return left or right or itself
        
        dfs(root)
        return self.res