# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node):
            if (   (p.val < node.val and node.val < q.val) 
                or (p.val > node.val and node.val > q.val)
                or node.val == p.val
                or node.val == q.val):
                return node # common ancestor
            
            if node.val > p.val: # lower values
                return dfs(node.left)
            else: # higher value
                return dfs(node.right)
        
        return dfs(root)
        