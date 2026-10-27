class MinStack:

    def __init__(self):
        self.stack = [] # Key = [val, minVal]

    def push(self, val: int) -> None:
        minVal = val if not self.stack or self.stack[-1][1] > val else self.stack[-1][1]
        self.stack.append([val, minVal])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
