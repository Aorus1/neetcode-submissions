class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(1 << n):
            subset = [nums[j] for j in range(n) if (i & (1 << j))]
            if subset in res:
                continue
            res.append(subset)
        return res[::-1]
            