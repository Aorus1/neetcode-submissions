from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        p, q = len(s1), len(s2)
        if (p + q) != len(s3):
            return False
        @cache
        def dp(i, j):                
            if i == p and j == q:
                return True
            k = i+j
            take1 = (i < p and s1[i] == s3[k] and dp(i+1, j))
            take2 = (j < q and s2[j] == s3[k] and dp(i, j+1))
            return take1 or take2

        return dp(0, 0)
        