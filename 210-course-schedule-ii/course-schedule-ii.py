from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # directed graph
        graph = defaultdict(list)
        for course, req in prerequisites:
            graph[course].append(req)
        
        res = []
        visiting = set()
        visited = set()
        def dfs(course): # True if allowed
            if course in visiting: # cycle detected
                return False
            if course in visited: # already visited
                return True
            
            visiting.add(course)

            if course in graph: # has prerequisites
                for req in graph[course]:
                    if not dfs(req):
                        return False

            visiting.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        for course in range(numCourses):
            if course not in visited and not dfs(course):
                return []
        
        return res