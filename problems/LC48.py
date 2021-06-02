# O(n*m)
# n = len(matrix) | m = len(matrix[0])

# Sol 1
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for y in range(len(matrix) // 2):
            for x in range(y, len(matrix) - y - 1):
                self.rotatePixel(matrix, y, x)

    def rotatePixel(self, matrix, y, x):
        # Upper-left to upper-right
        temp = matrix[x][-y - 1]
        matrix[x][-y - 1] = matrix[y][x]

        # Upper-right to lower-right
        temp, matrix[-y - 1][-x - 1] = matrix[-y - 1][-x - 1], temp

        # Lower-right to lower-left
        temp, matrix[-x - 1][y] = matrix[-x - 1][y], temp

        # Lower-right to upper-right
        matrix[y][x] = temp


# Sol 2
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transposeMatrix(matrix)
        self.reflectMatrix(matrix)

    def transposeMatrix(self, matrix):
        for y in range(len(matrix)):
            for x in range(y):
                self.swap(matrix, y, x, x, y)

    def reflectMatrix(self, matrix):
        for y in range(len(matrix)):
            for x in range(len(matrix[y]) // 2):
                self.swap(matrix, y, x, y, -x - 1)

    def swap(self, matrix, y1, x1, y2, x2):
        matrix[y1][x1], matrix[y2][x2] = matrix[y2][x2], matrix[y1][x1]