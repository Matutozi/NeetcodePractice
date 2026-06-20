class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")" : "(",
            "]":"[",
            "}":"{"
        }

        stack = []

        for char in s:
            if char in pairs:
                #check if the stack is not empty
                if stack and stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False
