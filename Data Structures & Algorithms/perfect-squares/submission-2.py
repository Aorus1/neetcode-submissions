from functools import cache
class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i*i for i in range(n+1, 0, -1) if i*i <= n]

        @cache
        def dp(total: int) -> int:
            if total == 0:
                return 0
            res = float("inf")
            for sq in squares:
                if sq > total:
                    continue
                res = min(res, 1+dp(total-sq))
            return res
                
                


        return dp(n)