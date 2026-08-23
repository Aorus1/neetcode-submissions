class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        total = 0

        min_heap = [(0, 0)]

        def dist(p1, p2):
            xi, yi = p1
            xj, yj = p2
            return abs(xi - xj) + abs(yi-yj)

        while min_heap:
            weight, current_node = heapq.heappop(min_heap)

            if current_node in visited:
                continue

            visited.add(current_node)
            total += weight
            for neighbor in range(n):
                if neighbor not in visited:
                    heapq.heappush(min_heap, (dist(points[neighbor], points[current_node]), neighbor))
        return total
        