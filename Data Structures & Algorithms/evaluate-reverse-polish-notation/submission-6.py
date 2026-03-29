class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokenStack = []
        
        for i in range(len(tokens)):
            if tokens[i] == "+":
                tokenStack.append(tokenStack.pop() + tokenStack.pop())
            elif tokens[i] == "-":
                tokenStack.append(tokenStack.pop() - tokenStack.pop())
            elif tokens[i] == "*":
                tokenStack.append(tokenStack.pop() * tokenStack.pop())
            elif tokens[i] == "/":
                tokenStack.append(int(tokenStack.pop() / tokenStack.pop()))
            else:
                tokenStack.append(int(tokens[i]))

        return tokenStack.pop()