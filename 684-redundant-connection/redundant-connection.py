class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = {} # node: parent

        def find(x):
            while nodes[x] != x:
                #nodes[x] = nodes[nodes[x]]
                x = nodes[x]
            return x

        def union(x, y): # return False if cycle
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False
            nodes[rootY] = rootX
            return True

        res = [-1, -1]

        for node, edge in edges:
            if node not in nodes:
                nodes[node] = node
            
            if edge not in nodes:
                nodes[edge] = edge
            
            if not union(node, edge):
                res = [node, edge]
                    
        return res
