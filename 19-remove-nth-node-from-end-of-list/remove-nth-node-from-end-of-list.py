# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # count size linked list
        curr = head
        i = 0
        while curr:
            i += 1
            curr = curr.next

        # traverse until previous node
        curr = head
        for _ in range(1, i - n):
            curr = curr.next
        
        # remove node
        if i - n == 0: return head.next

        temp = curr.next
        curr.next = curr.next.next

        return head
