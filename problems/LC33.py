# O(log(n))
# n = len(nums)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        rotationIndex = self.searchRotationIndex(nums)
        return self.rotatedBinarySearch(nums, target, rotationIndex)

    def searchRotationIndex(self, nums):
        start = 0
        end = len(nums)
        while start < end:
            midpoint = start + ((end - start) // 2)
            if midpoint == 0 or nums[midpoint] < nums[midpoint - 1]:
                return midpoint
            elif nums[midpoint] > nums[-1]:
                start = midpoint + 1
            else:
                end = midpoint

    def rotatedBinarySearch(self, nums, target, rotationIndex):
        start = rotationIndex
        end = rotationIndex + len(nums)
        while start < end:
            midpoint = start + ((end - start) // 2)
            trueMidpoint = midpoint % len(nums)
            if nums[trueMidpoint] == target:
                return trueMidpoint
            elif nums[trueMidpoint] < target:
                start = midpoint + 1
            else:
                end = midpoint
        return -1