# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(node, leaves):
            

            if node and node.left:
                dfs(node.left, leaves)
            if node and node.right:
                dfs(node.right, leaves)
            
            if node and not node.left and not node.right:
                leaves.append(node.val)

            return leaves
        
        return dfs(root1, []) == dfs(root2, [])

            