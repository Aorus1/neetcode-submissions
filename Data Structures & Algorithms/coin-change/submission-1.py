from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def bfs(amt): # bfs(amt) is number of coins needed
            if(amt == 0):
                return 0   
            if (amt in coins):
                return 1
            if amt < min(coins):
                return -1

            minval = -1
            for coin in coins:
                val = bfs(amt-coin)
                if val != -1:
                    minval = val if (minval == -1) else min(minval, val)
            if (minval == -1):
                return -1
            return minval + 1

        return bfs(amount)
 