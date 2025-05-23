import heapq
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visited = 0
        res = 0

        def dfs(node):
            if not node: return
            
            dfs(node.left)

            nonlocal visited
            visited += 1
            if visited == k:
                nonlocal res
                res = node.val
                return
                
            dfs(node.right)

        dfs(root)
        return res
