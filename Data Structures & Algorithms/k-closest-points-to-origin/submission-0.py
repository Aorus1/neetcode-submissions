class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = [(math.sqrt(x*x + y*y), [x, y]) for x, y in points]
        heapq.heapify(arr)
        return [a for _, a in heapq.nsmallest(k, arr)]