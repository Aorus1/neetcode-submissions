class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            premap[course].append(pre)

        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if premap[course] == []:
                return True
            visited.add(course)
            for pre in premap[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            premap[course] = []
            return True
            
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

                    

            

        