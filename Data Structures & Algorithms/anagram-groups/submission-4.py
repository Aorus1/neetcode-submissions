class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        hm = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for c in s:
                val = ord(c) - ord('a')
                key[val] += 1
            if tuple(key) in hm:
                hm[tuple(key)].append(s)
            else:
                hm[tuple(key)] = [s]
            
        return list(hm.values())
        