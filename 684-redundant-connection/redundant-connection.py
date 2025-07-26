class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = {} # node: parent

        def representative(node):
            while nodes[node] != node:
                node = nodes[node]
            return node

        res = [-1, -1]

        for node, edge in edges:
            if node not in nodes and edge not in nodes:
                nodes[node] = node
                nodes[edge] = node
                
            elif node not in nodes:
                nodes[node] = representative(edge)
            
            elif edge not in nodes:
                nodes[edge] = representative(node)
                
            else:
                # already in same group
                if representative(node) == representative(edge):
                    res = [node, edge]
                # not redundant connection - add connection
                else: 
                    nodes[representative(edge)] = node
                    
        return res
