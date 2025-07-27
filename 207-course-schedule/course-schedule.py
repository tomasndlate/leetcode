from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        visiting = set()
        visited = set()
        def isCycle(course): # dfs
            if course in visiting:
                return True
            if course in visited:
                return False
            
            visiting.add(course)
            if course in graph:
                for pre in graph[course]:
                    if isCycle(pre):
                        return True
            visiting.remove(course)
            visited.add(course)
        
        for course in graph.keys():
            if course not in visited and isCycle(course):
                return False
        
        return True
