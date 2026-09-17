class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []

        for t in tokens:
            if t in "+-*/":
                t2 = res.pop()
                t1 = res.pop()

                if t == "+":
                    res.append(t1 + t2)
                if t == "-":
                    res.append(t1 - t2)
                if t == "*":
                    res.append(t1 * t2)
                if t == "/":
                    res.append(int(t1 / t2))
            else:
                res.append(int(t))

        return res[-1]