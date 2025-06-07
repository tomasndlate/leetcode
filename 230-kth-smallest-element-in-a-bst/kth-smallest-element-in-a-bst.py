# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # DFS - KEEP TRACK OF NUMBER OF VISITED
        count = 0
        found = False
        value = 0

        def dfs(node):
            nonlocal count, value, found
            if not node or found: return
            dfs(node.left)
            count += 1
            if count == k:
                value = node.val
            dfs(node.right)
        
        dfs(root)
        return value
        