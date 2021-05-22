# O(log(n))
# n = len(nums)


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [
            self.binarySearch(nums, target, True),
            self.binarySearch(nums, target, False),
        ]

    def binarySearch(self, nums, target, searchingFirst):
        start = 0
        end = len(nums)
        while start < end:
            midpoint = start + ((end - start) // 2)
            if nums[midpoint] == target:
                if searchingFirst:
                    if midpoint == 0 or nums[midpoint - 1] != target:
                        return midpoint
                    end = midpoint
                else:
                    if midpoint == len(nums) - 1 or nums[midpoint + 1] != target:
                        return midpoint
                    start = midpoint + 1
            elif nums[midpoint] > target:
                end = midpoint
            else:
                start = midpoint + 1
        return -1