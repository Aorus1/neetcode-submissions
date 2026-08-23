class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        neighbors = {i: [] for i in range(n+1)}
        dist = [float("inf")] * (n+1)



        for source, target, delay in times:
            neighbors[source].append((target, delay))
            
        q = []
        for i in range(1, n+1):
            heapq.heappush(q, (dist[i], i))

        dist[k] = 0
        dist[0] = 0
        
        while q:
            _, u = heapq.heappop(q)
            for v, delay in neighbors[u]:
                temp = dist[u] + delay
                if temp < dist[v]:
                    dist[v] = temp
                    heapq.heappush(q, (dist[v], v))
        if float("inf") in dist:
            return -1
        return max(dist)

        