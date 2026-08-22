class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        best = 0
        l = 0
        r = 0

        while r < len(s):
            if s[r] in chars: # if we've already seen this character in current substring
                while s[r] != s[l]: # then as long as left is not equal to new string
                    chars.remove(s[l])
                    l += 1
                l+=1
                r+=1
            else:
                chars.add(s[r])
                best = max(best, r-l+1)
                r += 1
        return best
            

            


        
            
            



        