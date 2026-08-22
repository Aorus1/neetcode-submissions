class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        cc = 0
        adj_list = {i: [] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def dfs(node):
            visited.add(node)
            for neigh in adj_list[node]:
                if neigh not in visited:
                    dfs(neigh)

        for node in range(0, n):
            if node not in visited:
                cc += 1
                dfs(node)

        return cc
