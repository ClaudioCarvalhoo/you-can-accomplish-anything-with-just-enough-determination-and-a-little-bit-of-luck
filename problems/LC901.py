class StockSpanner:
    # O(1)
    def __init__(self):
        self.spanStack = []

    # O(n) | Amortized O(1)
    def next(self, price: int) -> int:
        curSpan = 1
        while len(self.spanStack) > 0 and self.spanStack[-1][0] <= price:
            curSpan += self.spanStack.pop()[1]
        self.spanStack.append((price, curSpan))
        return curSpan
