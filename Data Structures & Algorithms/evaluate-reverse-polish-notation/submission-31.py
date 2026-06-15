class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0

        for token in tokens:
            if token in '+-*/':
                a, b = stack.pop(), stack.pop()

                if token == '+':
                    res = a + b
                    stack.append(res)
                elif token == '-':
                    res = b - a
                    stack.append(res)
                elif token == '*':
                    res = a * b
                    stack.append(res)
                elif token == '/':
                    res = int(b / a)
                    stack.append(res)
            else:
                stack.append(int(token))

        return stack[-1]