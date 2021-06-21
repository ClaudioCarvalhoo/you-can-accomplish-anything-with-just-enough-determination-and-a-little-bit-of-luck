# O(n³)
# n = len(nums)


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()
        seen = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    complement = target - (nums[i] + nums[j] + nums[k])
                    if complement in seen:
                        res.add((complement, nums[i], nums[j], nums[k]))
            seen.add(nums[i])
        return res