# O(n)
# n = len(position)

from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        atEven = 0
        atOdd = 0
        for i in position:
            if i % 2 == 0:
                atEven += 1
            else:
                atOdd += 1

        needToChangeParity = min(atEven, atOdd)

        return needToChangeParity