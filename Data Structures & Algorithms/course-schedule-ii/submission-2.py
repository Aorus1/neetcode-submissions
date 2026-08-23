class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        L = []
        indeg = [0] * numCourses
        q = deque()


        # build adj list
        premap = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            premap[b].append(a)
            indeg[a] += 1
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)

        print(q)
        
        while q:
            course = q.popleft()
            L.append(course)
            for neigh in premap[course]:
                indeg[neigh] -= 1
                if (indeg[neigh] == 0):
                    q.append(neigh)

        if len(L) != numCourses:
            return []
        else:
            return L


        
        

        
        