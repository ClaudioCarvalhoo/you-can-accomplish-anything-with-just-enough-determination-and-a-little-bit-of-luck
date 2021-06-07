# O(2ⁿ)
# n = len(nums)


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.explore(nums, 0, [], res)
        return res

    def explore(self, nums, start, cur, res):
        for i in range(start, len(nums)):
            cur.append(nums[i])
            self.explore(nums, i + 1, cur, res)
            cur.pop()
        res.append(cur[:])