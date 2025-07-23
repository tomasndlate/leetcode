# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for order, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, order, l))

        dummy = ListNode()
        cur = dummy

        while heap:
            val, order, l = heapq.heappop(heap)
            cur.next = l
            cur = cur.next
            if l.next:
                heapq.heappush(heap, (l.next.val, order, l.next))
        
        return dummy.next
        