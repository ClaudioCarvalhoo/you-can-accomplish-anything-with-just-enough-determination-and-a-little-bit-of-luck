# O(n)
# n = len(nums)


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        inArray = set()
        for elem in nums:
            if elem in inArray:
                return True
            inArray.add(elem)
        return False