# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node, path):
            nonlocal res
            if not node:
                return

            path.append(node.val)
            if not node.left and not node.right:
                res += int("".join(map(str, path)))
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            path.pop()
        
        dfs(root, [0])
        return res