# O(n)
# n = len(nums)

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        res = []
        rangeStart = nums[0]
        for i in range(len(nums)):
            if i == len(nums) - 1:
                res.append(self.makeOutputElement(rangeStart, nums[i]))
            elif rangeStart == None:
                rangeStart = nums[i]
            elif nums[i + 1] != nums[i] + 1:
                res.append(self.makeOutputElement(rangeStart, nums[i]))
                rangeStart = nums[i + 1]
        return res

    def makeOutputElement(self, rangeStart, rangeEnd):
        if rangeStart == None or rangeStart == rangeEnd:
            return str(rangeEnd)
        else:
            return str(rangeStart) + "->" + str(rangeEnd)