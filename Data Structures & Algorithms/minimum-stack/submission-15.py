class MinStack:

    def __init__(self):
        self.stack = [] # [val, minVal]

    def push(self, val: int) -> None:
        minVal = val if not self.stack or val < self.stack[-1][1] else self.stack[-1][1]
        self.stack.append([val, minVal])

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
