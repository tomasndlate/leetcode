from collections import defaultdict
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = defaultdict(list) # node: [edges]
        for node, edge in edges:
            nodes[node].append(edge)
            nodes[edge].append(node)
        
        visited = set()
        groups = defaultdict(set)
        def dfs(node, group):
            visited.add(node)
            groups[group].add(node)
            for edge in nodes[node]:
                if edge not in visited:
                    dfs(edge, group)

        completeGroups = 0
        for i in range(n):
            if i in visited:
                continue
                
            dfs(i, i)

            complete = True
            for node in groups[i]:
                if len(nodes[node]) != len(groups[i]) - 1:
                    complete = False
                    continue
                    
            if complete:
                completeGroups += 1

        return completeGroups