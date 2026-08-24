from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        @cache
        def dp(i): # dp(i) is the minimum cost to reach step i
            if i == 0:
                return 0
            if i == 1:
                return 0
            
            return min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])

        
        return dp(n)
        