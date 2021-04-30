# O(n)
# n = len(nums)


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        largest = nums[:3]
        smallest = nums[:3]
        largest.sort()
        smallest.sort()
        for num in nums[3:]:
            if num > largest[0]:
                largest[0] = num
                largest.sort()
            if num < smallest[2]:
                smallest[2] = num
                smallest.sort()
        return max(
            largest[0] * largest[1] * largest[2], largest[2] * smallest[0] * smallest[1]
        )
