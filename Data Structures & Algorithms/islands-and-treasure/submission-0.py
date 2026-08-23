class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])

        # q is queue of coords of treasure
        q = deque()

        # starting queue contains all treasure chests
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        
        # while new nodes to explore
        while q:
            (i, j) = q.pop() # pop node
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]: # for each neighbor
                if (i+di < 0 or i+di >= m or j+dj < 0 or j+dj >= n or grid[i+di][j+dj] in [-1, 0]): # if OOB or not land
                    continue
                # if untouched land, keep propagating
                if grid[i+di][j+dj] == 2147483647:
                    q.appendleft((i+di, j+dj))
                grid[i+di][j+dj] = min(grid[i+di][j+dj], 1 + grid[i][j])


        return
        