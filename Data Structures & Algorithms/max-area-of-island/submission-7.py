class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxarea = 0

        visited = set()


        def dfs(i, j):
            if (i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1 or (i, j) in visited):
                return 0
            area = 1
            visited.add((i, j))
            grid[i][j] = 0
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                area += dfs(i + di, j + dj)
            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = dfs(i, j)
                    maxarea = max(area, maxarea)
        
        
        return(maxarea)

            
            
