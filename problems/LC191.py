# O(n)
# n = len(n) in bits


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            if n % 2 != 0:
                count += 1
            n = n >> 1
        return count
