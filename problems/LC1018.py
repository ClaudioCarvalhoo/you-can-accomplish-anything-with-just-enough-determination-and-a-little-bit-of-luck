# O(n)
# n = len(A)

from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        current = 0
        for element in A:
            if element:
                current = current * 2 + 1
            else:
                current = current * 2

            if current % 5 == 0:
                res.append(True)
            else:
                res.append(False)

        return res
