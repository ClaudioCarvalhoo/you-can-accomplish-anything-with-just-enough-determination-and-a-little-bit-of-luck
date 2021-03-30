# Longest Consecutive Sequence

# O(n)
# n = len(nums)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ranges = {}
        existing = set(nums)

        maxRangeLength = 0
        for num in nums:
            rangeSize = self.explore(num, ranges, existing)
            maxRangeLength = max(maxRangeLength, rangeSize)
        return maxRangeLength

    def explore(self, num, ranges, existing):
        if num not in existing:
            return 0
        if num not in ranges:
            ranges[num] = 1 + self.explore(num + 1, ranges, existing)
        return ranges[num]
