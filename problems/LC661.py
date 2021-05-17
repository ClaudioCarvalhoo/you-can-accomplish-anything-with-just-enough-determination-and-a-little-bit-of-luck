# O(n*m)
# n = len(img) | m = len(img[0])


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        res = [[0 for _ in range(len(img[0]))] for _ in range(len(img))]
        for y in range(len(img)):
            for x in range(len(img[y])):
                res[y][x] = self.getAverage(img, y, x)
        return res

    def getAverage(self, img, y, x):
        totalSum = 0
        totalCount = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= y + i < len(img) and 0 <= x + j < len(img[y]):
                    totalSum += img[y + i][x + j]
                    totalCount += 1
        return totalSum // totalCount