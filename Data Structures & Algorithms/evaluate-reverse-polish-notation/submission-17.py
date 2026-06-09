class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oppr_stack = []

        for t in tokens:
            if t == "+":
                oppr_stack.append(oppr_stack.pop() + oppr_stack.pop())

            elif t == "-":
                num2, num1 = oppr_stack.pop(), oppr_stack.pop()
                oppr_stack.append(num1 - num2)

            elif t == "*":
                oppr_stack.append(oppr_stack.pop() * oppr_stack.pop())

            elif t == "/":
                num2, num1 = oppr_stack.pop(), oppr_stack.pop()
                oppr_stack.append(int(num1 / num2))

            else:
                oppr_stack.append(int(t))

        return oppr_stack[0]