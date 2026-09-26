class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in "+-*/":
                v2 = stack.pop()
                v1 = stack.pop()

                if t == "+":
                    stack.append(v1 + v2)

                elif t == "-":
                    stack.append(v1 - v2)

                elif t == "*":
                    stack.append(v1 * v2)

                elif t == "/":
                    stack.append(int(v1 / v2))
            else:
                stack.append(int(t))
        
        return stack[-1]