class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for node, dependency in prerequisites:
            graph[dependency].append(node)
        
        visited = set()
        visiting = set()

        def dfs(node): # return true if found cycle
            if node in visiting: return True # cycle
            if (   node in visited
                or node not in graph):
                return False

            visited.add(node)
            visiting.add(node)
            for neighbor in graph[node]:
                if dfs(neighbor): return True
            visiting.remove(node)
            return False

        for node in graph:
            if dfs(node): # has cycle - cannot finish course
                return False
        return True