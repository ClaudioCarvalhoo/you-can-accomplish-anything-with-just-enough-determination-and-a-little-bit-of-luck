# O(1)

from typing import List


class Solution:
    def validSquare(
        self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]
    ) -> bool:
        points = sorted([p1, p2, p3, p4], key=lambda point: (point[0], point[1]))
        return (
            self.dist(points[0], points[1]) != 0
            and self.dist(points[0], points[1]) == self.dist(points[1], points[3])
            and self.dist(points[1], points[3]) == self.dist(points[3], points[2])
            and self.dist(points[3], points[2]) == self.dist(points[2], points[0])
            and self.dist(points[0], points[3]) == self.dist(points[1], points[2])
        )

    def dist(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
