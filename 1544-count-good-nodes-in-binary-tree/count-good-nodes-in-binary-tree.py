# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node:TreeNode, prev:int) -> int:
            if not node: return 0
            res = 0
            
            if node.val >= prev:
                res += 1
                prev = node.val

            res += dfs(node.left, prev)
            res += dfs(node.right, prev)
            return res
        
        return dfs(root, float('-inf'))

        