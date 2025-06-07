# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def dfs_depth(node):
            nonlocal balanced
            if not node: return 0
            
            left = dfs_depth(node.left)
            right = dfs_depth(node.right)

            if abs(left - right) > 1:
                balanced = False
            
            return 1 + max(left, right)
        
        dfs_depth(root)
        return balanced
            