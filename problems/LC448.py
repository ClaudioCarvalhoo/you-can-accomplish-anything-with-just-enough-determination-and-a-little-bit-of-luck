# O(n) Time | O(1) Space
# n = len(nums)


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            self.putInPlace(nums, nums[i])
        res = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(i + 1)
        return res

    def putInPlace(self, nums, i):
        if nums[i - 1] == i:
            return
        temp = nums[i - 1]
        nums[i - 1] = i
        self.putInPlace(nums, temp)