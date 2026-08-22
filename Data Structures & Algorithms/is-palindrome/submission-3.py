class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(char.lower() for char in s if char.isalnum())
        l, r = 0, len(string) - 1 # left and right pointers
        while l < r:
            if string[l] != string[r]:
                return False
            l+=1
            r-=1
        return True
        