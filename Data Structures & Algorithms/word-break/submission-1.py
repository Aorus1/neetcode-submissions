from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        @cache
        def recur(i):
            if i == n:
                return True
            for word in wordDict:
                if s[i:].startswith(word):
                    if recur(i+len(word)):
                        return True
            return False
            
            
            

        return recur(0)