from functools import cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        @cache
        def dp(targ):
            if targ == 0:
                return 1
            res = 0
            for i in range(len(nums)):
                if targ < nums[i]:
                    break
                res += dp(targ-nums[i])
            return res
        return dp(target)
                