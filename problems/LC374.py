# O(log(n))

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        start = 0
        end = n + 1
        while start < end:
            midpoint = start + ((end - start) // 2)
            res = guess(midpoint)
            if res == 0:
                return midpoint
            elif res > 0:
                start = midpoint + 1
            else:
                end = midpoint
        return None