from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0:
            return False

        targ = total / 2
        


        @cache
        def dp(i, j): # using up to index i, can we form sum j
            if j == 0:
                return True
            if i == 0:
                return False
            if nums[i-1] <= j:
                return dp(i-1, j) or dp(i-1, j-nums[i-1])
            else:
                return dp(i-1, j)

        return dp(n-1, targ)

            



            
        
        