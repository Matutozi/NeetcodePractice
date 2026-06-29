class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operand = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in operand:
                stack.append(int(token))

            if token in operand:
                second = stack.pop()
                first = stack.pop()
                if token == "+":
                    result = first + second
                elif token == "-":
                    result = first - second
                elif token == "*":
                    result = first * second
                else:
                    result = int(first / second)
                stack.append(result)
        return stack[-1]