# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root: return None

        newright = self.invertTree(root.left)
        newleft = self.invertTree(root.right)

        root.left = newleft 
        root.right = newright

        return root
        