class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))


        edge_reachable = set()
        q = deque()
        for i in range(m):
            for j in range(n): # iterate over all values
                if ((i == 0 or i == m-1) or (j == 0 or j == n-1)) and board[i][j] == "O": #if on edge
                    q.append((i, j))
                    edge_reachable.add((i, j))
        # do BFS
        while q:
            i, j = q.popleft()
            for di, dj in dirs:
                ni, nj = i+di, j+dj
                if (0 < ni < m-1 and 0 < nj < n-1) and (board[ni][nj] == "O") and ((ni, nj) not in edge_reachable):
                    edge_reachable.add((ni, nj))
                    q.append((ni, nj))


        for i in range(m):
            for j in range(n):
                if (i, j) not in edge_reachable and board[i][j] == "O":
                    board[i][j] = "X"
                
        return








