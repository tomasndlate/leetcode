# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        balanced = True

        def dfs(curr):
            if not curr: return 0
            depthleft = dfs(curr.left)
            depthright = dfs(curr.right)

            if abs(depthleft - depthright) > 1:
                nonlocal balanced
                balanced = False
            
            return 1 + max(depthleft, depthright)
        
        dfs(root)
        return balanced
        