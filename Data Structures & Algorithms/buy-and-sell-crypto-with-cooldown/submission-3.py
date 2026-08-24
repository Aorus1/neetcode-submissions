from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dp(i: int, own: bool): # dp(i, own) is additional profit i can make starting from day i
            if i >= n:
                return 0
            if own: # sell today or hold
                return max(prices[i] + dp(i+2, False), dp(i+1, True))
            else: # buy today or wait
                return max(dp(i+1, True) - prices[i], dp(i+1, False))
        return dp(0, False)
            