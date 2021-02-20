# O(n)
# n = len(s)


class Solution:
    def maxPower(self, s: str) -> int:
        currentCount = 0
        currentChar = ""
        power = 1
        for char in s:
            if char == currentChar:
                currentCount += 1
                power = max(power, currentCount)
            else:
                currentChar = char
                currentCount = 1
        return power