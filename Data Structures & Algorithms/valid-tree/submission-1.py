class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # simple check if right number of edges, can early return if not
        if len(edges) != n-1:
            return False

        # build adj list
        adj_list = {i: [] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for neigh in adj_list[node]: #connected nodes
                if (neigh == parent):
                    continue
                if neigh in visited:
                    return False
                if not dfs(neigh, node):
                    return False
            return True
        if not dfs(0, -1):
            return False
        return len(visited) == n


        

        
        