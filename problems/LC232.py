class MyQueue:

    # O(1)
    def __init__(self):
        self.pseudoQueue = []
        self.temporaryStack = []
        self.front = None

    # O(1)
    def push(self, x: int) -> None:
        if len(self.temporaryStack) == 0:
            self.front = x
        self.temporaryStack.append(x)

    # O(1) Amortized | O(n) Worst Case
    def pop(self) -> int:
        if len(self.pseudoQueue) == 0:
            while len(self.temporaryStack) > 0:
                self.pseudoQueue.append(self.temporaryStack.pop())
        return self.pseudoQueue.pop()

    # O(1)
    def peek(self) -> int:
        if len(self.pseudoQueue) > 0:
            return self.pseudoQueue[-1]
        return self.front

    # O(1)
    def empty(self) -> bool:
        return len(self.pseudoQueue) == 0 and len(self.temporaryStack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()