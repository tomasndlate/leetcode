# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # Find middle
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse 2nd half, and Unattach 1st half from 2nd half
        prev = None
        cur = slow.next
        slow.next = None

        while cur:
            temp = cur.next
            cur.next = prev
            # update pointers
            prev = cur
            cur = temp
        
        # Find maximum
        l1 = head
        l2 = prev
        maxSum = 0

        while l1 and l2:
            maxSum = max(maxSum, l1.val + l2.val)
            l1 = l1.next
            l2 = l2.next
        
        return maxSum