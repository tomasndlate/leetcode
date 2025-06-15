class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {} # course: [pre]
        for course, pre in prerequisites:
            if course not in preMap:
                preMap[course] = []
            preMap[course].append(pre)
        
        visited = set()
        visiting = set()
        def detectCycle(course):
            if course in visiting:
                return True
            if course in visited:
                return False
            
            visiting.add(course)
            for pre in preMap.get(course, []):
                if detectCycle(pre):
                    return True

            visiting.remove(course)
            visited.add(course)
            return False
        
        # loop through courses, and check cycles
        for c in range(numCourses):
            if detectCycle(c):
                return False
        
        return True