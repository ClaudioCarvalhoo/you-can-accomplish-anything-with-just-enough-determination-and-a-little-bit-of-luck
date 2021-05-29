# O(log(n))
# n = x


class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x + 1
        while start < end:
            midpoint = start + ((end - start) // 2)
            midSquare = midpoint * midpoint
            nextMidSquare = (midpoint + 1) * (midpoint + 1)
            if midSquare == x or (midSquare < x and nextMidSquare > x):
                return midpoint
            elif midSquare < x:
                start = midpoint + 1
            else:
                end = midpoint