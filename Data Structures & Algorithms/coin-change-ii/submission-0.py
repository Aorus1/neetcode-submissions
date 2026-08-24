from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        @cache
        def dp(i, amt):
            if amt == 0:
                return 1
            if i == n or amt < 0:
                return 0

            use = dp(i, amt - coins[i])
            skip = dp(i+1, amt)
            return use + skip
        return dp(0, amount)
            