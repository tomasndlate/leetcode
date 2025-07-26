# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(node): # TreeNode
            if not node:
                return None
            if not node.left and not node.right:
                return node

            flatLeft = dfs(node.left)

            if flatLeft:
                flatLeft.left, flatLeft.right = None, node.right
                node.left, node.right = None, node.left

                right = flatLeft.right

            else:
                right = node.right
            
            flatRight = dfs(right)

            return flatRight if flatRight else flatLeft
        
        dfs(root)
        return root
            
        