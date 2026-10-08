class MinStack:

    def __init__(self):
        self.stack = [] # val, min

    def push(self, val: int) -> None:
        minVal = self.stack[-1][1] if self.stack and self.stack[-1][1] < val else val
        self.stack.append([val, minVal])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
