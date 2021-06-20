# O(n*m)
# n = len(matrix) | m = len(matrix[0])


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        upBound = -1
        rightBound = len(matrix[0])
        downBound = len(matrix)
        leftBound = -1

        res = [matrix[0][0]]
        y = 0
        x = 0
        while rightBound - leftBound > 1 and downBound - upBound > 1:
            while x + 1 < rightBound:
                x += 1
                res.append(matrix[y][x])
            upBound = y

            while y + 1 < downBound:
                y += 1
                res.append(matrix[y][x])
            rightBound = x

            if rightBound - leftBound <= 1 or downBound - upBound <= 1:
                break

            while x - 1 > leftBound:
                x -= 1
                res.append(matrix[y][x])
            downBound = y

            while y - 1 > upBound:
                y -= 1
                res.append(matrix[y][x])
            leftBound = x
        return res
