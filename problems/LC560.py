# O(n)
# n = len(nums)


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        foundSums = {0: 1}
        cumulativeSum = 0
        for num in nums:
            cumulativeSum += num
            differenceToTarget = cumulativeSum - k
            if differenceToTarget in foundSums:
                res += foundSums[differenceToTarget]
            if cumulativeSum not in foundSums:
                foundSums[cumulativeSum] = 0
            foundSums[cumulativeSum] += 1
        return res