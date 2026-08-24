from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        def dp(i, targ):
            ways = 0

            if i == n-1:
                if targ == nums[i]:
                    ways += 1
                if targ == -nums[i]:
                    ways += 1
                return ways

            ways += dp(i+1, targ - nums[i])
            ways += dp(i+1, targ + nums[i])
            return ways
        return dp(0, target)
            


        