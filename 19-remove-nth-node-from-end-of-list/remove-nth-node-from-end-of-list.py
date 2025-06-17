# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = second = dummy = ListNode(next=head)
        for _ in range(n):
            first = first.next
        
        while first and first.next:
            first = first.next
            second = second.next
        
        # Remove next of second
        second.next = second.next.next
        #prev = second
        #second = second.next.next # skip remove
        #prev.next = second
        
        return dummy.next
