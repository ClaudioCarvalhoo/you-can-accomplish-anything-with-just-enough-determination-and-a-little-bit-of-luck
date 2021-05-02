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


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        while i < len(prices):
            boughtFor = prices[i]
            while i < len(prices) - 1 and prices[i] < prices[i + 1]:
                i += 1
            profit += max(0, prices[i] - boughtFor)
            i += 1
        return profit