# O(n)
# n = len(s)


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        bestOnes = 0
        bestZeros = 0
        curOnes = 0
        curZeros = 0
        for char in s:
            if char is "0":
                curZeros += 1
                curOnes = 0
            if char is "1":
                curOnes += 1
                curZeros = 0
            bestZeros = max(bestZeros, curZeros)
            bestOnes = max(bestOnes, curOnes)
        return bestOnes > bestZeros