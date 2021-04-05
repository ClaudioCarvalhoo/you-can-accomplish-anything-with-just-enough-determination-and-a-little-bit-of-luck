# O(n²)
# n = len(nums)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums) - 2):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                if nums[i] + nums[start] + nums[end] == 0:
                    res.add((nums[i], nums[start], nums[end]))
                    start += 1
                elif nums[i] + nums[start] + nums[end] > 0:
                    end -= 1
                else:
                    start += 1
        res = [list(x) for x in res]
        return res