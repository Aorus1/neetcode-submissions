class Solution:
    def climbStairs(self, n: int) -> int:
        dp0 = 1
        dp1 = 1
        for _ in range(2, n+1):
            temp = dp0 + dp1
            dp0 = dp1
            dp1 = temp
        return dp1