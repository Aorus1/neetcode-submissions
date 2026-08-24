from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        p = len(s1)
        q = len(s2)
        if (p + q) != len(s3):
            return False
        @cache
        def dp(i, j):                
            if i == p and j == q:
                return True
            if (i != p and s1[i] == s3[i+j]):
                if(dp(i+1, j)):
                    return True
            if (j != q and s2[j] == s3[i+j]):
                if(dp(i, j+1)):
                    return True
            return False

        return dp(0, 0)
        