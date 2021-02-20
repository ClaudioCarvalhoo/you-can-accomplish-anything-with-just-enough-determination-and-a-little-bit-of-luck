# O(1) technically since there are only 45 possible combinations

from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        queue = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        while len(queue) > 0:
            elem = queue.pop(0)
            if low <= elem <= high:
                res.append(elem)
            lastDigit = elem % 10
            if lastDigit < 9:
                queue.append((elem * 10) + lastDigit + 1)
        return res