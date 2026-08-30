class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        n = len(s)
        l, r = 0, 0
        maxlen = 0
        chars = set()
        chars.add(s[l])
        while l != n-1:
            if r == n-1:
                return maxlen
            while s[r+1] in chars:
                chars.remove(s[l])
                l += 1
            r += 1
            chars.add(s[r])
            maxlen = max(maxlen, r - l + 1)
        return maxlen


            # zxyzxyz
            #  123
            


            
            
                






