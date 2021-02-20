# O(k * log(n))
# k = k | n = len(matrix)

import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if k == 1:
            return matrix[0][0]

        elems = []
        for i in range(len(matrix)):
            heapq.heappush(elems, (matrix[i][0], 0, i))

        used = 0
        while len(elems) > 0:
            number, column, row = heapq.heappop(elems)
            used += 1
            if used == k:
                return number
            elif column + 1 < len(matrix[row]):
                heapq.heappush(elems, (matrix[row][column + 1], column + 1, row))

        return matrix[-1][-1]