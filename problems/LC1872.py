# O(n)
# n = len(stones)


class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        res = sum(stones)
        prefixSum = res - stones[-1]
        for i in range(len(stones) - 2, 0, -1):
            res = max(res, prefixSum - res)
            prefixSum -= stones[i]
        return res