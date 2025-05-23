import heapq
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if node:
                heapq.heappush(heap, -node.val)
                if len(heap) > k:
                    heapq.heappop(heap)
                queue.append(node.left)
                queue.append(node.right)
        
        return -heapq.heappop(heap)
