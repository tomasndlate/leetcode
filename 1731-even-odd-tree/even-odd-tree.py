# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            False
        queue = deque([root])
        level = 0

        while queue:
            n = len(queue)
            for i in range(n):
                if level % 2 == 0: # even level
                    if (queue[i].val % 2 == 0) or (i > 0 and queue[i].val <= queue[i-1].val):
                        return False
                    continue
                
                if level % 2 != 0: # odd level
                    if (queue[i].val % 2 != 0) or (i > 0 and queue[i].val >= queue[i-1].val):
                        return False
                    continue
            level += 1

            for _ in range(n):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return True
