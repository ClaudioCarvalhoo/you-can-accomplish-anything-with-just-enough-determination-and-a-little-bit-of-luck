# O(n)
# n = len(num) in bits

from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]

        answers = [-1 for x in range(num + 1)]
        answers[0] = 0
        answers[1] = 1

        for i in range(2, num + 1):
            aditional = i % 2
            answers[i] = answers[i >> 1] + aditional

        return answers[: num + 1]
