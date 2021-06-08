import random


class Solution:

    # O(n)
    def __init__(self, w: List[int]):
        self.ranges = []
        curWeightSum = 0
        for weight in w:
            curWeightSum += weight
            self.ranges.append(curWeightSum)

    # O(log(n))
    def pickIndex(self) -> int:
        num = random.randint(1, self.ranges[-1])
        start = 0
        end = len(self.ranges)
        while start < end:
            midpoint = start + ((end - start) // 2)
            if self.ranges[midpoint] >= num and (
                midpoint == 0 or self.ranges[midpoint - 1] < num
            ):
                return midpoint
            elif self.ranges[midpoint] < num:
                start = midpoint + 1
            else:
                end = midpoint


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()