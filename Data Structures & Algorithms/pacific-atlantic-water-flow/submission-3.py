class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(i, j, ocean, k):
            if (i, j) in ocean or i < 0 or j < 0 or i == ROWS or j == COLS or heights[i][j] < k:
                return
            ocean.add((i, j))
            dfs(i+1, j, ocean, heights[i][j])
            dfs(i-1, j, ocean, heights[i][j])
            dfs(i, j+1, ocean, heights[i][j])
            dfs(i, j-1, ocean, heights[i][j])






        visited = set()
        for i in range(ROWS):
            dfs(i, 0, pac, 0)


        for i in range(1, COLS):
            dfs(0, i, pac, 0)

        for i in range(ROWS):
            dfs(i, COLS-1, atl, 0)


        for i in range(0, COLS-1):
            dfs(ROWS-1, i, atl, 0)

        return list(pac  & atl)