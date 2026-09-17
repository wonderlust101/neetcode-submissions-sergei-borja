class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []

        for t in tokens:
            if t in "+-*/":
                t2 = int(res.pop())
                t1 = int(res.pop())

                if t == "+":
                    res.append(t1 + t2)
                if t == "-":
                    res.append(t1 - t2)
                if t == "*":
                    res.append(t1 * t2)
                if t == "/":
                    res.append(t1 / t2)
            else:
                res.append(t)

        return int(res[-1])