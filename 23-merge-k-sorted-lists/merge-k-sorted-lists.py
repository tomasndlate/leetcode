# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for order, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, order, head))
        
        dummy = ListNode()
        cur = dummy

        while heap:
            value, order, node = heapq.heappop(heap)

            if node.next:
                heapq.heappush(heap, (node.next.val, order, node.next))

            cur.next = node
            cur = cur.next
        
        return dummy.next
        