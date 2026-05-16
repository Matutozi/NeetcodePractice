class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}

        for course, vals in prerequisites:
            preMap[course].append(vals)

        setVal = set()
        def dfs(course):
            if course in setVal:
                return False
            
            if preMap[course] == []:
                return True

            setVal.add(course)

            for i in preMap[course]:
                if not dfs(i):
                    return False

            setVal.remove(course)
            preMap[course] = []

            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
                


        