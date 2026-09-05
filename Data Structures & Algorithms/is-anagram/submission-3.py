class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a1 = defaultdict(int)
        a2 = defaultdict(int)
        for c in s:
            a1[c] += 1
        for c in t:
            a2[c] += 1
        return a1 == a2