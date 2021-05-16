import collections


class FindSumPairs:

    # O(n2)
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums2Table = collections.Counter(nums2)

    # O(1)
    def add(self, index: int, val: int) -> None:
        self.nums2Table[self.nums2[index]] -= 1
        self.nums2[index] += val
        if self.nums2[index] in self.nums2Table:
            self.nums2Table[self.nums2[index]] += 1
        else:
            self.nums2Table[self.nums2[index]] = 1

    # O(n1)
    def count(self, tot: int) -> int:
        res = 0
        for num in self.nums1:
            needed = tot - num
            if needed in self.nums2Table:
                res += self.nums2Table[needed]
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)