# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        # return depth
        def dfs(curr) -> int:
            if not curr: return 0

            depthleft = dfs(curr.left)
            depthright = dfs(curr.right)

            self.diameter = max(self.diameter, depthleft + depthright)

            return 1 + max(depthleft, depthright)

        dfs(root)
        return self.diameter
        