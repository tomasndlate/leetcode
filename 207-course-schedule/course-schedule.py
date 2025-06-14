class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        requisites = {} # course: [requisites]
        for course, req in prerequisites:
            if course not in requisites:
                requisites[course] = []
            requisites[course].append(req)

        visited = set()
        visiting = set()
        def detectCycle(c):
            if c in visiting:
                return True
            if c in visited or c not in requisites:
                return False
            
            visiting.add(c)
            for req in requisites[c]:
                if detectCycle(req):
                    return True
            visiting.remove(c)
            visited.add(c)
            return False
        
        for req in range(numCourses):
            if detectCycle(req):
                return False
                
        return True
            