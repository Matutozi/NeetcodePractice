class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []

        for ch in s:
            # Opening bracket
            if ch in "([{":
                stack.append(ch)

            # Closing bracket
            else:
                # No matching opening bracket
                if not stack:
                    return False

                top = stack.pop()

                # Wrong type of opening bracket
                if top != pairs[ch]:
                    return False

        # All opening brackets must be matched
        return len(stack) == 0