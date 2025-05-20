# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        extra = 0

        while l1 or l2 or extra:

            total = 0

            if l1: total += l1.val; l1 = l1.next
            if l2: total += l2.val; l2 = l2.next
            total += extra
            
            num = total % 10
            extra = total // 10

            curr.next = ListNode(num)
            curr = curr.next
        
        return dummy.next

        