class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [99999] * n
        dp[0] = 0
        for i in range(n):
            jump = nums[i]
            for j in range(jump+1):
                if i + j >= n:
                    continue
                dp[i+j] = min(dp[i] + 1, dp[i+j])
        return dp[n-1]
            

            
        