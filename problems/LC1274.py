# O(log(n*m)) Because of constraint of ships <= 10
# n = topRight.x - bottomLeft.x | m = topRight.y - bottomLeft.y

# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
# class Point(object):
# 	def __init__(self, x: int, y: int):
# 		self.x = x
# 		self.y = y


class Solution(object):
    def countShips(self, sea: "Sea", topRight: "Point", bottomLeft: "Point") -> int:
        return self.explore(sea, bottomLeft, topRight)

    def explore(self, sea, bottomLeft, topRight):
        if (
            bottomLeft.x > topRight.x
            or bottomLeft.y > topRight.y
            or not sea.hasShips(topRight, bottomLeft)
        ):
            return 0
        if bottomLeft.x == topRight.x and bottomLeft.y == topRight.y:
            return 1
        middle = Point(
            bottomLeft.x + ((topRight.x - bottomLeft.x) // 2),
            bottomLeft.y + ((topRight.y - bottomLeft.y) // 2),
        )
        q1 = (bottomLeft, middle)
        q2 = (Point(middle.x + 1, bottomLeft.y), Point(topRight.x, middle.y))
        q3 = (Point(bottomLeft.x, middle.y + 1), Point(middle.x, topRight.y))
        q4 = (Point(middle.x + 1, middle.y + 1), topRight)
        res = 0
        for nextQuadrant in [q1, q2, q3, q4]:
            res += self.explore(sea, nextQuadrant[0], nextQuadrant[1])
        return res