# Time
# O(n*m)
# n = len(A) | m = len(A[0])

# Space
# O(1)
# Due to making it in-place in the input

import math
from typing import List

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            for i in range(math.ceil(len(row)/2)):
                temp = row[i]
                row[i] = self.invert(row[-i-1])
                row[-i-1] = self.invert(temp)
        return A
                
                
    def invert(self, value):
        if value == 0:
            return 1
        else:
            return 0