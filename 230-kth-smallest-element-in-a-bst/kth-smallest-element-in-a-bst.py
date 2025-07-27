# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kth = 0
        kth_val = None

        def dfs(node):
            nonlocal kth, kth_val
            if not node or kth_val != None:
                return
            
            dfs(node.left)
            kth += 1
            if kth == k:
                kth_val = node.val
            dfs(node.right)
        
        dfs(root)
        return kth_val
