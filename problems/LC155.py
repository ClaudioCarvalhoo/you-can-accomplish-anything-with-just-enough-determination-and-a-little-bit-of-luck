class MinStack:

    # O(1)
    def __init__(self):
        self.stack = []
        self.aux = []

    # O(1)
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.aux) == 0 or val <= self.aux[-1]:
            self.aux.append(val)

    # O(1)
    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.aux[-1]:
            self.aux.pop()
        return val

    # O(1)
    def top(self) -> int:
        return self.stack[-1]

    # O(1)
    def getMin(self) -> int:
        return self.aux[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()