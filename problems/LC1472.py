# Sol 1
class BrowserHistory:

    # O(1)
    def __init__(self, homepage: str):
        self.currentUrl = homepage
        self.backStack = []
        self.forwardStack = []

    # O(1)
    def visit(self, url: str) -> None:
        self.backStack.append(self.currentUrl)
        self.currentUrl = url
        self.forwardStack = []

    # O(n)
    def back(self, steps: int) -> str:
        for _ in range(min(steps, len(self.backStack))):
            self.forwardStack.append(self.currentUrl)
            self.currentUrl = self.backStack.pop()
        return self.currentUrl

    # O(n)
    def forward(self, steps: int) -> str:
        for _ in range(min(steps, len(self.forwardStack))):
            self.backStack.append(self.currentUrl)
            self.currentUrl = self.forwardStack.pop()
        return self.currentUrl


# Sol 2
class BrowserHistory:

    # O(1)
    def __init__(self, homepage: str):
        self.visits = [homepage]
        self.currentPosition = 0
        self.maxForward = 0

    # O(1)
    def visit(self, url: str) -> None:
        if self.currentPosition + 1 >= len(self.visits):
            self.visits.append(url)
        else:
            self.visits[self.currentPosition + 1] = url
        self.currentPosition += 1
        self.maxForward = self.currentPosition

    # O(1)
    def back(self, steps: int) -> str:
        self.currentPosition = max(0, self.currentPosition - steps)
        return self.visits[self.currentPosition]

    # O(1)
    def forward(self, steps: int) -> str:
        self.currentPosition = min(self.maxForward, self.currentPosition + steps)
        return self.visits[self.currentPosition]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)