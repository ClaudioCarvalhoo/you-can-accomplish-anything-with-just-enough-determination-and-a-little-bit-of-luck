# O(n)
# n = len(mat)


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        for i in range(len(mat)):
            res += mat[i][i]
            if i != len(mat) - 1 - i:
                res += mat[i][-i - 1]

        return res