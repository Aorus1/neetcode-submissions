from functools import cache
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        @cache
        def dp(i): # dp(i) is true or false, depending on whether you can reach last index from index i
            if i >= n:
                return False
            if i == n-1:
                return True
            if nums[i] + i >= n-1:
                return True
            for j in range(1, nums[i]+1):
                if (dp(i+j)):
                    return True
            return False

        return dp(0)

        