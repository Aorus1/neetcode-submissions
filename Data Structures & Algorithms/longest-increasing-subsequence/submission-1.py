from functools import cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(i):
            if i == n-1:
                return 1
            maxval = 1
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    maxval = max(maxval, 1 + dp(j))
            return maxval


        return max([dp(i) for i in range(n)])

