# O(n)
# n = len(prices)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = [0 for _ in range(len(prices))]
        minToLeft = prices[0]
        for i in range(1, len(prices)):
            left[i] = max(left[i - 1], prices[i] - minToLeft)
            minToLeft = min(minToLeft, prices[i])

        right = [0 for _ in range(len(prices))]
        maxToRight = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            right[i] = max(right[i + 1], maxToRight - prices[i])
            maxToRight = max(maxToRight, prices[i])

        best = 0
        for i in range(len(prices)):
            best = max(best, left[i] + right[i])
        return best