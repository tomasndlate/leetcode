class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependencies = {}

        for course, pre in prerequisites:
            if course not in dependencies:
                dependencies[course] = []
            dependencies[course].append(pre)

        visited = set()
        visiting = set()
        def valid(course):
            if course in visiting: return False
            if course in visited: return True
            
            visiting.add(course)

            for pre in dependencies.get(course, []):
                if not valid(pre):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            return True
        
        for course in range(numCourses):
            if not valid(course): return False

        return True