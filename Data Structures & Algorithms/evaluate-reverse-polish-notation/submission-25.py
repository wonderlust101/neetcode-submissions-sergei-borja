class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        token_queue = []

        for token in tokens:
            if token in "+-*/":
                a, b = token_queue.pop(), token_queue.pop()

                if token == '+':
                    res = a + b
                    token_queue.append(res)
                if token == '-':
                    res = b - a
                    token_queue.append(res)
                if token == '*':
                    res = a * b
                    token_queue.append(res)
                if token == '/':
                    res = int(b / a)
                    token_queue.append(res)
            else:
                token_queue.append(int(token))
                
        return int(token_queue[-1])