import heapq


class MedianFinder:

    # O(1)
    def __init__(self):
        self.leftSide = []
        self.rightSide = []

    # O(log(n))
    def addNum(self, num: int) -> None:
        if len(self.leftSide) == 0 or num < self.findMedian():
            heapq.heappush(self.leftSide, -num)
        else:
            heapq.heappush(self.rightSide, num)
        self._adjustSides()

    # O(1)
    def findMedian(self) -> float:
        if len(self.rightSide) == 0:
            return -self.leftSide[0]
        if (len(self.leftSide) + len(self.rightSide)) % 2 != 0:
            if len(self.leftSide) > len(self.rightSide):
                return -self.leftSide[0]
            else:
                return self.rightSide[0]
        else:
            return ((-self.leftSide[0]) + self.rightSide[0]) / 2

    def _adjustSides(self):
        if len(self.leftSide) > len(self.rightSide) + 1:
            num = -heapq.heappop(self.leftSide)
            heapq.heappush(self.rightSide, num)
        elif len(self.rightSide) > len(self.leftSide) + 1:
            num = heapq.heappop(self.rightSide)
            heapq.heappush(self.leftSide, -num)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()