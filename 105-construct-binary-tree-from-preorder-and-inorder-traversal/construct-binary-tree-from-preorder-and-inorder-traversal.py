# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(val=preorder[0])

        root_i = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:root_i + 1], inorder[:root_i])
        root.right = self.buildTree(preorder[root_i + 1:], inorder[root_i + 1:])

        return root
        