# O(sqrt(n))
# n = num

import math
from typing import List


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        goal1 = num + 1
        goal2 = num + 2

        closest1 = self.findClosestDivisorsForGoal(goal1)
        closest2 = self.findClosestDivisorsForGoal(goal2)

        if abs(closest1[0] - closest1[1]) < abs(closest2[0] - closest2[1]):
            return closest1
        else:
            return closest2

    def findClosestDivisorsForGoal(self, goal):
        for i in range(math.floor(math.sqrt(goal)), 0, -1):
            if goal / i % 1 == 0:
                return [i, goal // i]
        return [1, goal]