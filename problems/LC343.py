# O(n)
# n = n


class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        threes = 0
        twos = 0
        while n > 2:
            n -= 3
            threes += 1
        if n == 2:
            twos = 1
        elif n == 1:
            threes -= 1
            twos += 2

        return 3 ** threes * 2 ** twos
