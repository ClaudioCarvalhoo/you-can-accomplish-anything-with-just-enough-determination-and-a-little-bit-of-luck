# O(n) Time | O(1) Space
# n = len(nums)


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        whiteStart = 0
        blueStart = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                self.swap(nums, i, whiteStart)
                whiteStart += 1
            if nums[i] == 1:
                self.swap(nums, i, blueStart)
                blueStart += 1
            blueStart = max(blueStart, whiteStart)

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
