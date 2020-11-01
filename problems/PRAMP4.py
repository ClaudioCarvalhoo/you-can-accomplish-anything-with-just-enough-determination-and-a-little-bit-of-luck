# Matrix Spiral Copy
# Given a 2D array (matrix) inputMatrix of integers,
# create a function spiralCopy that copies inputMatrix’s values into a 1D array in a spiral order, clockwise.
# Your function then should return that array. Analyze the time and space complexities of your solution.

# Example:
# input:  inputMatrix  = [ [1,    2,   3,  4,    5],
#                          [6,    7,   8,  9,   10],
#                          [11,  12,  13,  14,  15],
#                          [16,  17,  18,  19,  20] ]

# output: [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]

# Time:
# O(n*m)
# n = len(inputMatrix) | m = len(inputMatrix[0])

# Space:
# O(1)


def spiral_copy(inputMatrix):
    if len(inputMatrix) == 0:
        return []
    if len(inputMatrix) == 1:
        return inputMatrix[0]
    if len(inputMatrix[0]) == 1:
        res = []
        for row in inputMatrix:
            res.append(row[0])
        return res

    horizontalMoves = len(inputMatrix[0]) - 1
    verticalMoves = len(inputMatrix) - 1

    res = []
    for i in range(len(inputMatrix[0])):
        res.append(inputMatrix[0][i])

    x = len(inputMatrix[0]) - 1
    y = 0
    while horizontalMoves > 0 and verticalMoves > 0:
        for i in range(1, verticalMoves + 1):
            y += 1
            res.append(inputMatrix[y][x])
        verticalMoves -= 1

        for i in range(1, horizontalMoves + 1):
            x -= 1
            res.append(inputMatrix[y][x])
        horizontalMoves -= 1

        if horizontalMoves <= 0 or verticalMoves <= 0:
            break

        for i in range(1, verticalMoves + 1):
            y -= 1
            res.append(inputMatrix[y][x])
        verticalMoves -= 1

        for i in range(1, horizontalMoves + 1):
            x += 1
            res.append(inputMatrix[y][x])
        horizontalMoves -= 1

    return res
