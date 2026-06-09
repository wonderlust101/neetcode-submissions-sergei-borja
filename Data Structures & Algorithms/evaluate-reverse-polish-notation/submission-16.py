class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oppr_stack = []

        valid_oppr = ["+", "-", "*", "/"]

        for t in tokens:
            if t in valid_oppr:
                num2 = oppr_stack.pop()
                num1 = oppr_stack.pop()

                if t == "+":
                    oppr_stack.append(num1 + num2)
                elif t == "-":
                    oppr_stack.append(num1 - num2)
                elif t == "*":
                    oppr_stack.append(num1 * num2)
                elif t == "/":
                    oppr_stack.append(int(num1 / num2))

            else:
                oppr_stack.append(int(t))

        return oppr_stack[0]