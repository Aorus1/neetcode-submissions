import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for num in nums:
            hm[num] = hm.get(num, 0) + 1

        result = [(k, v) for k, v in hm.items()]
        print(result)
        output = heapq.nsmallest(k, result, key=lambda x: -x[1])
        return([x for (x, y) in output])
    

        