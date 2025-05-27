"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        hashmap = {}
        # traverse and create hashmap with node -> newnode
        queue = collections.deque()
        queue.append(node)
        while queue:
            cur = queue.popleft()
            hashmap[cur] = Node(cur.val)
            for neigh in cur.neighbors:
                if neigh not in hashmap:
                    queue.append(neigh)

        # traverse hasmap and add ref for each neighbor new node
        visited = set()
        queue.append(node)
        while queue:
            cur = queue.popleft()
            if cur in visited: continue
            visited.add(cur)
            for neigh in cur.neighbors:
                # add ref to new node
                hashmap[cur].neighbors.append(hashmap[neigh])
                if neigh not in visited:
                    queue.append(neigh)
        
        return hashmap[node]
        