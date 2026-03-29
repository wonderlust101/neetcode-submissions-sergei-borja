class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokenStack = []
        
        for i in range(len(tokens)):
            if not tokens[i] == "+" or not tokens[i] == "-" or not tokens[i] == "*" or not tokens[i] == "/":
                tokenStack.append(int(tokens[i]))
                continue
            
            b = tokenStack.pop()
            a = tokenStack.pop()
            
            if tokens[i] == "+":
                tokenStack.append(a + b)
            if tokens[i] == "-":
                tokenStack.append(a - b)
            if tokens[i] == "*":
                tokenStack.append(a * b)
            if tokens[i] == "/":
                tokenStack.append(int(a / b))

        return tokenStack.pop()