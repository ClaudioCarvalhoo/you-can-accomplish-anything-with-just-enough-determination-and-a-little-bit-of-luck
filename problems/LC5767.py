# O(n*log(n))
# n = len(ranges)


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort(key=lambda x: x[0])
        i = 0
        while i < len(ranges) and ranges[i][1] < left:
            i += 1
        if i >= len(ranges) or ranges[i][0] > left:
            return False

        rightmostFound = ranges[i][1]
        while i < len(ranges) and ranges[i][1] < right:
            if i + 1 >= len(ranges) or ranges[i + 1][0] - 1 > rightmostFound:
                break
            i += 1
            rightmostFound = max(rightmostFound, ranges[i][1])

        return rightmostFound >= right
