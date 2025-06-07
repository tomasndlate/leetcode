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
        # LINKED LIST
        dummy = ListNode(next=head)

        # Find middle
        slow, fast = dummy, dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Revert pointer to point back (slow is the last of 1st half)
        cur = slow.next
        prev = None
        slow.next = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        # Merge both lists
        l1, l2 = head, prev # prev contains last value 2nd list
        while l1 and l2:
            temp1, temp2 = l1.next, l2.next
            l1.next = l2
            l2.next = temp1
            l1, l2 = temp1, temp2
        
        return head
        
