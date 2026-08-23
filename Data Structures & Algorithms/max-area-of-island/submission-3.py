from functools import cache
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxarea = 0

        visited = set()

        q = deque()

        @cache
        def dfs(i, j):
            if (i < 0 or i > m-1 or j < 0 or j > n-1 or grid[i][j] != 1):
                return 0
            count = 1
            visited.add((i, j))
            if ((i+1, j) not in visited):
                count += dfs(i+1, j)
            if ((i-1, j) not in visited):
                count += dfs(i-1, j)
            if ((i, j+1) not in visited):
                count += dfs(i, j+1)
            if ((i, j-1) not in visited):
                count += dfs(i, j-1)
            return count

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    area = dfs(i, j)
                    maxarea = max(area, maxarea)
        
        
        return(maxarea)

            
            
