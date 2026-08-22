class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        res = []
        def dfs(i, j, k):
            nonlocal pacific, atlantic            

            if i < 0 or j < 0:
                pacific = True
                return
            if i >= len(heights) or j >= len(heights[0]):
                atlantic = True
                return
            if (i, j) in visited or (pacific and atlantic):
                return

            if heights[i][j] > k:
                return
            visited.add((i, j))

            
            dfs(i-1, j, min(k, heights[i][j]))
            dfs(i, j-1, min(k, heights[i][j]))


            dfs(i+1, j, min(k, heights[i][j]))
            dfs(i, j+1, min(k, heights[i][j]))





        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                visited = set()
                pacific = False
                atlantic = False
                dfs(i, j, heights[i][j])
                if pacific and atlantic:
                    res.append([i, j])
        return res
        
        