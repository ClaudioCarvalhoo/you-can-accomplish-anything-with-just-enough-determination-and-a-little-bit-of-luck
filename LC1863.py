# O(n)
# n = len(nums)


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            for i in range(len(res)):
                res.append(res[i] ^ num)
            res.append(num)
        return sum(res)