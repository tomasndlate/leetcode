# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        imbalanced = False

        def dfs_depth(node):
            nonlocal imbalanced
            if not node: return 0
            
            left = dfs_depth(node.left)
            right = dfs_depth(node.right)

            if abs(left - right) > 1:
                imbalanced = True
            
            return 1 + max(left, right)
        
        dfs_depth(root)
        return not imbalanced
            