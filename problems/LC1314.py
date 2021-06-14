# O(n*m)
# n = len(mat) | m = len(mat[0])


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        blockSum = self.buildBlockSum(mat)
        res = [[0 for _ in mat[0]] for _ in mat]
        for y in range(len(mat)):
            for x in range(len(mat[y])):
                lowerY = max(0, y - k)
                higherY = min(len(mat) - 1, y + k)
                leftX = max(0, x - k)
                rightX = min(len(mat[higherY]) - 1, x + k)
                res[y][x] += blockSum[higherY][rightX]
                if lowerY > 0:
                    res[y][x] -= blockSum[lowerY - 1][rightX]
                if leftX > 0:
                    res[y][x] -= blockSum[higherY][leftX - 1]
                if lowerY > 0 and leftX > 0:
                    res[y][x] += blockSum[lowerY - 1][leftX - 1]
        return res

    def buildBlockSum(self, mat):
        blockSum = [[0 for _ in mat[0]] for _ in mat]
        for y in range(len(mat)):
            for x in range(len(mat[y])):
                blockSum[y][x] += mat[y][x]
                if y > 0:
                    blockSum[y][x] += blockSum[y - 1][x]
                if x > 0:
                    blockSum[y][x] += blockSum[y][x - 1]
                if y > 0 and x > 0:
                    blockSum[y][x] -= blockSum[y - 1][x - 1]
        return blockSum
