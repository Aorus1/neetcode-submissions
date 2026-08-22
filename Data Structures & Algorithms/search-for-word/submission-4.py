class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.present = False

        

        def dfs(i, j, k):

            if (i >= len(board) or j >= len(board[0]) or i < 0 or j < 0):
                return
            if (i, j) in self.visited:
                return

            if (board[i][j] != word[k]):
                return

            self.visited.add((i, j))

            if (k == len(word) - 1):
                self.present = True
                return
            dfs(i+1, j, k+1)
            dfs(i-1, j, k+1)
            dfs(i, j+1, k+1)
            dfs(i, j-1, k+1)

            self.visited.remove((i, j))


        for i in range(len(board)):
            for j in range(len(board[0])):
                self.visited = set()
                dfs(i, j, 0)
                
        return self.present





        