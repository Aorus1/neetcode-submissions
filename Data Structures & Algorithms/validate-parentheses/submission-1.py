class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in [")", "}", "]"]:
                if not stack:
                    return False
                top = stack.pop()
                if char == ")" and top == "(":
                    continue
                if char == "}" and top == "{":
                    continue
                if char == "]" and top == "[":
                    continue
                return False

            else:
                stack.append(char)
        if not stack:
            return True
        else:
            return False

        