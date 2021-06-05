# O(n)
# n = n


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        res = 1
        product = 1
        multiplier = 9
        for i in range(n):
            product *= multiplier
            res += product
            if i > 0:
                multiplier -= 1
        return res
