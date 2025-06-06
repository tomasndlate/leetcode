"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        copies = {}

        cur = head
        while cur:
            copies[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            if cur.next: copies[cur].next = copies[cur.next]
            if cur.random: copies[cur].random = copies[cur.random]
            cur = cur.next
        
        return copies[head]
        