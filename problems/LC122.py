# O(n)
# n = len(prices)

import math
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        valueBought = math.inf
        for i in range(len(prices)):
            if valueBought < prices[i]:
                profit += prices[i] - valueBought
            valueBought = prices[i]

        return profit
