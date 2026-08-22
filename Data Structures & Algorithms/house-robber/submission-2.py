class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n # dp[i] represents the max amount you can get from all houses up to house i

        if n < 2:
            return nums[0]

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[n-1]


        