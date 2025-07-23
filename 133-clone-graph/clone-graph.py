"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        clones = {}
        queue = deque([node])

        while queue:
            cur = queue.popleft()
            if cur not in clones:
                clones[cur] = Node(val=cur.val)

            for neigh in cur.neighbors:
                if neigh not in clones:
                    clones[neigh] = Node(val=neigh.val)
                    queue.append(neigh)
                clones[cur].neighbors.append(clones[neigh])
        
        return clones[node]