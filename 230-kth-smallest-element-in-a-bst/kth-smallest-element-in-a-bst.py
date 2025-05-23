# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visited = 0
        stack = []
        cur = root

        while cur or stack:
            # explore left
            while cur:
                stack.append(cur)
                cur = cur.left
            
            # process node
            cur = stack.pop()
            visited += 1
            if visited == k:
                return cur.val

            # go right
            cur = cur.right