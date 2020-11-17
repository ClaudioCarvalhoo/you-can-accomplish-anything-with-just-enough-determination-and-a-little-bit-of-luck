# O(n)
# n = len(A)

from typing import List

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        best = 0
        cur = 1
        goingUp = True
        for i in range(1, len(A)):
            if goingUp:
                if A[i] > A[i-1]:
                    cur += 1
                elif A[i] < A[i-1] and cur > 1:
                    cur += 1
                    goingUp = False
                else:
                    cur = 1
            else:
                if A[i] < A[i-1]:
                    cur += 1
                elif A[i] > A[i-1]:
                    cur = 2
                    goingUp = True
                else:
                    cur = 1
                    goingUp = True   
                    
            if not goingUp:
                best = max(best, cur)
            
        if best < 3:
            best = 0
        return best
        