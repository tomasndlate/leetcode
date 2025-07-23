# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None

        def findLCA(node) -> bool:
            if not node:
                return False
            
            itself = node == p or node == q
            left = findLCA(node.left)
            right = findLCA(node.right)

            if itself + left + right >= 2:
                nonlocal lca
                lca = node
            return itself or left or right
        
        findLCA(root)
        return lca