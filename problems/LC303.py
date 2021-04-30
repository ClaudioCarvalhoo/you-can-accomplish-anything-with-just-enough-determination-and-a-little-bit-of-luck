class NumArray:

    # O(n)
    # n = len(nums)
    def __init__(self, nums: List[int]):
        self.sumToLeft = [0]
        for num in nums:
            self.sumToLeft.append(self.sumToLeft[-1] + num)

    # O(1)
    def sumRange(self, left: int, right: int) -> int:
        return self.sumToLeft[right + 1] - self.sumToLeft[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)