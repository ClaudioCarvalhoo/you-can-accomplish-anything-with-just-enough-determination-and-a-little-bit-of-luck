# O(n)
# n = len(arr)


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        for i in range(len(arr)):
            oddsToLeft = i // 2
            oddsToRight = (len(arr) - i - 1) // 2
            evensToLeft = i - oddsToLeft
            evensToRight = len(arr) - i - 1 - oddsToRight
            appearsInOddSubarray = (
                1
                + oddsToLeft
                + oddsToRight
                + (oddsToLeft * oddsToRight)
                + (evensToLeft * evensToRight)
            )
            res += arr[i] * appearsInOddSubarray
        return res