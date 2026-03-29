class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokenStack = []

        validOperations = ["+", "-", "*", "/"]
        
        for i in range(len(tokens)):
            if not tokens[i] in validOperations:
                tokenStack.append(int(tokens[i]))
                continue
            
            a = tokenStack.pop()
            b = tokenStack.pop()

            if tokens[i] == "+":
                tokenStack.append(a + b)
            if tokens[i] == "-":
                tokenStack.append(a - b)
            if tokens[i] == "*":
                tokenStack.append(a * b)
            if tokens[i] == "/":
                tokenStack.append(a / b)

        return tokenStack.pop()