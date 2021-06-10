# O(n*log(n))
# n = len(nums)


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSortCalc(nums, 0, len(nums))

    def mergeSortCalc(self, nums, start, end):
        if start == end - 1:
            return 0

        midpoint = start + ((end - start) // 2)
        leftRes = self.mergeSortCalc(nums, start, midpoint)
        rightRes = self.mergeSortCalc(nums, midpoint, end)
        leftToRightRes = self.reversePairsSortedSubarrays(nums, start, midpoint, end)
        self.merge(nums, start, midpoint, end)
        return leftRes + rightRes + leftToRightRes

    def merge(self, nums, start, midpoint, end):
        merged = []
        i1 = start
        i2 = midpoint
        while i1 < midpoint and i2 < end:
            if nums[i1] < nums[i2]:
                merged.append(nums[i1])
                i1 += 1
            else:
                merged.append(nums[i2])
                i2 += 1
        while i1 < midpoint:
            merged.append(nums[i1])
            i1 += 1
        while i2 < end:
            merged.append(nums[i2])
            i2 += 1
        for i in range(len(merged)):
            nums[start + i] = merged[i]

    def reversePairsSortedSubarrays(self, nums, start, midpoint, end):
        res = 0
        i2 = midpoint
        for i1 in range(start, midpoint):
            while i2 < end and nums[i1] > 2 * nums[i2]:
                i2 += 1
            res += i2 - midpoint
        return res