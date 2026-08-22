class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        l = 0
        ans = 0
        maxf = 0

        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r], 0) + 1
            maxf = max(maxf, hm[s[r]])

            while (r - l + 1) - maxf > k:
                hm[s[l]] -= 1
                l += 1   
            ans = max(ans, r - l + 1)         

        return ans
        
