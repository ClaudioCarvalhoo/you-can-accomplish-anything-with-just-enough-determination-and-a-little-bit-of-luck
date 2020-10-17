# O(1)

from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
            return False

        distx01 = points[1][0] - points[0][0]
        disty01 = points[1][1] - points[0][1]

        distx02 = points[2][0] - points[0][0]
        disty02 = points[2][1] - points[0][1]

        if disty01 == 0 or disty02 == 0:
            if disty01 == 0 and disty02 == 0:
                return False
            else:
                return True

        factor = distx01 / disty01

        if distx02 / disty02 == factor:
            return False
        else:
            return True


a = Solution()
print(a.isBoomerang([[0, 1], [1, 0], [0, 1]]))
