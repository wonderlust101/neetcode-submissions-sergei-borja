class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        tokenStack = []

        validOperations = ["+", "-", "*", "/"]
        
        for i in range(len(tokens)):
            if not tokens[i] in validOperations:
                tokenStack.append(int(tokens[i]))
                continue
            
            while len(tokenStack) > 0:
                if tokens[i] == "+":
                    res += tokenStack.pop()
                if tokens[i] == "-":
                    res -= tokenStack.pop()
                if tokens[i] == "*":
                    res *= tokenStack.pop()
                if tokens[i] == "/":
                    res /= tokenStack.pop()
            
        return res