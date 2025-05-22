# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = collections.deque()
        if root: queue.append(root)

        while queue:
            qlen = len(queue) # go through all level
            for i in range(qlen):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                if i == qlen - 1: res.append(node.val) #last node in level
        
        return res
        