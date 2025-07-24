# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kth = 0
        kth_node = None

        def dfs(node):
            nonlocal kth, kth_node
            if not node or kth_node:
                return

            dfs(node.left)

            kth += 1
            if kth == k:
                kth_node = node
                return

            dfs(node.right)
        
        dfs(root)
        return kth_node.val

            