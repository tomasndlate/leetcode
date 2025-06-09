# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root: return 0

        def dfs(node, threshold):
            if not node:
                return 0
            if node.val < threshold: # not valid
                return dfs(node.left, threshold) + dfs(node.right, threshold)
                
            return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
        
        return dfs(root, root.val)
        