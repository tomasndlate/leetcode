# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        maxSum = float('-inf')

        def dfs(node):
            nonlocal maxSum
            if not node:
                return 0
            
            itself = node.val
            # 0 avoids including if negative
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            curSum = itself + left + right
            maxSum = max(maxSum, curSum)

            return itself + max(left, right)
        
        dfs(root)
        return maxSum