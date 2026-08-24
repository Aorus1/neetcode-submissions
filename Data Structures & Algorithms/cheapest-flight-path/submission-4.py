class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i: [] for i in range(n)}
        dist = [float("inf")] * n

        for source, dest, price in flights:
            graph[source].append((price, dest))

        dist[src] = 0

        for i in range(k+1):
            next_dist = dist[:]
            for u, v, price in flights:
                next_dist[v] = min(next_dist[v], dist[u] + price)
            dist = next_dist
        return -1 if dist[dst] == float("inf") else dist[dst]

