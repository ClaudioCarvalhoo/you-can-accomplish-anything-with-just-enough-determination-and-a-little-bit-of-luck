# O(n)
# n = len(A)

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B) or len(A) <= 1:
            return False
        
        present = {}
        hasRepetition = False
        hasDifference = False
        differenceSolved = False
        diffA = ''
        diffB = ''
        
        for i in range(len(A)):
            if A[i] != B[i]:
                if differenceSolved:
                    return False
                
                if hasDifference:
                    if A[i] == diffB and B[i] == diffA:
                        differenceSolved = True
                    else:
                        return False
                    
                else:
                    diffA = A[i]
                    diffB = B[i]
                    hasDifference = True
                    
            else:
                if A[i] in present:
                    hasRepetition = True
                else:
                    present[A[i]] = True
                
        return (hasDifference and differenceSolved) or ((not hasDifference) and hasRepetition)