class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        if len(s) % 2 == 1: # if odd num of characters
            return False

        hm = {")":"(", "}":"{", "]":"["} #hm
        open = {"{", "(", "["}
        stack = deque()
        for c in s:
            if c in open:
                stack.appendleft(c)
                continue
            # c not in open, guaranteed
            if not stack:
                return False
            if hm[c] != stack.popleft():
                return False
        return(not stack)
            




