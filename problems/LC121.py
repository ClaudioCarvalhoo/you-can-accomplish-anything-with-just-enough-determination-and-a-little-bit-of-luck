# O(n)
# n = len(prices)

import math
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        smallest = math.inf
        for price in prices:
            smallest = min(smallest, price)
            profit = max(profit, price - smallest)

        return profit
