from functools import cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dp(targ):
            if targ == 0:
                return 1
            res = 0
            for num in nums:
                if num <= targ:
                    res += dp(targ - num)
            return res
        return dp(target)
                