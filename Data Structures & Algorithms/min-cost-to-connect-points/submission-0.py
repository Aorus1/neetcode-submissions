class UnionFind:
    def __init__(self, size: int):
        self.rank = [1] * size
        self.parent = list(range(size))
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        return x
    def union(self, a, b) -> bool:
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return False
        if self.rank[a] > self.rank[b]:
            self.parent[b] = self.find(a)
        elif self.rank[a] < self.rank[b]:
            self.rank[a] = self.find(b)
        else:
            self.parent[a] = self.find(b)
            self.rank[a] += 1
        return True
            
        

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = UnionFind(n)
        def dist(p1, p2):
            xi, yi = p1
            xj, yj = p2
            return abs(xi-xj) + abs(yi-yj)
        graph = [[dist(points[i], points[j]) for i in range(n)] for j in range(n)]
        edges = []
        for i in range(n):
            for j in range(i):
                edges.append((graph[i][j], i, j))
        edges.sort()

        ans = 0
        for dist, u, v in edges:
            if dsu.find(u) != dsu.find(v):
                ans += dist
                dsu.union(dsu.find(u), dsu.find(v))
        return ans


            
        