class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}

        while len(tokens) > 1:
            for t in range(len(tokens)):
                if tokens[t] in operators:
                    a = int(tokens[t-2])
                    b = int(tokens[t-1])

                    if tokens[t] == "+":
                        result = a + b
                    
                    elif tokens[t] == "-":
                        result = a - b
                    elif tokens[t] == "*":
                        result = a * b
                    else:
                        result = int(a / b)

                    tokens = (tokens[:t-2] + [str(result)] + tokens[t+1:])

                    break
        return int(tokens[0])
