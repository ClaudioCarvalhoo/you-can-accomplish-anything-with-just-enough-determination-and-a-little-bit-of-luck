# O(len(n) in bits)


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32, 0, -1):
            bit = n % 2
            res += bit
            if i > 1:
                res <<= 1
                n >>= 1
        return res
