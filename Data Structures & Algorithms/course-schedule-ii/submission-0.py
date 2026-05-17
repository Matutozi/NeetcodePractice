class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i:[] for i in range(numCourses)}

        for cre, preq in prerequisites:
            prereq[cre].append(preq)

        output = []
        visit, cycle = set(), set()

        def dfs(cre):
            if cre in cycle:
                return False
            if cre in visit:
                return True

            cycle.add(cre)
            for pre in prereq[cre]:
                if dfs(pre) == False:
                    return False
            cycle.remove(cre)
            visit.add(cre)
            output.append(cre)
            return True
            

        for course in range(numCourses):
            if dfs(course) == False:
                return []

        return output
    



                