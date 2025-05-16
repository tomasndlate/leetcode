# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find mid
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse 2nd half
        second = slow.next
        slow.next = None
        prev = None
        
        while second:
            nexttemp = second.next
            second.next = prev
            prev = second
            second = nexttemp

        # merge linked lists
        l1, l2 = head, prev
        
        # code here
        while l2:
            temp_l1, temp_l2 = l1.next, l2.next

            l2.next = temp_l1
            l1.next = l2

            l2 = temp_l2
            l1 = l1.next.next


        return head
        