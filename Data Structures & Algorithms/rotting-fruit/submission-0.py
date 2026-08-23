class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        q = deque()

        for i in range(m):
            for j in range(n):
                if (grid[i][j] == 2):
                    q.append((i, j, 0))

        maxtime = 0
        while q:
            i, j, t= q.popleft()
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if (0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1):
                    q.append((ni, nj, t+1))
                    grid[ni][nj] = 2
                    maxtime = max(maxtime, t+1)
        for i in range(m):
            for j in range(n):
                if (grid[i][j] == 1):
                    return -1
        return maxtime

        