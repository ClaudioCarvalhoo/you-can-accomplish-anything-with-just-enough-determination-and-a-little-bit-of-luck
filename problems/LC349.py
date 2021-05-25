# O(n+m)
# n = len(nums1) | m = len(nums2)


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        nums1 = set(nums1)
        for num in nums2:
            if num in nums1:
                res.add(num)
        return list(res)