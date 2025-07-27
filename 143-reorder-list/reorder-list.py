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
        if not head:
            return None
        
        # Find mid node
        slow = fast = ListNode(next=head)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Unlink both halfs
        second = slow.next
        slow.next = None

        # Revert 2nd half
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # Merge both halfs
        first = head
        second = prev
        while first and second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
        
        return head