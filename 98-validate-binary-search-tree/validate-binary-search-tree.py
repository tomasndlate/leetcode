# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(node, leftBound, rightBound):
            if not node:
                return True
            
            if node.val <= leftBound or rightBound <= node.val:
                return False
            
            return isValid(node.left, leftBound, node.val) and isValid(node.right, node.val, rightBound)
        
        return isValid(root, float('-inf'), float('inf'))