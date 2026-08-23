class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        neighbors = {i: [] for i in range(1, n+1)}
        dist = [float("inf")] * (n+1)



        for source, target, delay in times:
            neighbors[source].append((target, delay))
            
        q = [(0, k)]

        dist[k] = 0
        
        while q:
            curr_dist, u = heapq.heappop(q)
            if curr_dist > dist[u]:
                continue
            for v, delay in neighbors[u]:
                new_dist = curr_dist + delay
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(q, (new_dist, v))
        ans = max(dist[1:])
        return -1 if ans == float("inf") else ans

        