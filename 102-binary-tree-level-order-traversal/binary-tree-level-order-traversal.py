from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        queue = deque([ [root] ])
        res = []

        while queue:
            level = queue.popleft()
            visited = []
            tovisit = []

            for node in level:
                visited.append(node.val)
                if node.left:
                    tovisit.append(node.left)
                if node.right:
                    tovisit.append(node.right)

            if tovisit: queue.append(tovisit)
            if visited: res.append(visited)
        
        return res

        