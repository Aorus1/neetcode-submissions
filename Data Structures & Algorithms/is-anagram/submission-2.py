class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        n = len(s)
        hm1 = defaultdict(int)
        hm2 = defaultdict(int)
        for i in range(n):
            hm1[s[i]] += 1
            hm2[t[i]] += 1
        return hm1 == hm2
