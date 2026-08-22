from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)

        @cache
        def dp(i, j):
            if i<0 or i>=n1 or j<0 or j>=n2:
                return 0
            if i == 0 and j == 0:
                if text1[i] == text2[j]:
                    return 1
            if text1[i] == text2[j]:
                return 1 + dp(i-1, j-1)
            return max(dp(i-1, j), dp(i, j-1))

            

        return dp(n1-1, n2-1)
        
