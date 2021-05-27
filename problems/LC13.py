# O(n)
# n = len(s)


class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        subtractIfNext = {
            "I": set(["V", "X"]),
            "X": set(["L", "C"]),
            "C": set(["D", "M"]),
        }

        res = 0
        for i in range(len(s)):
            multiplier = 1
            if (
                i + 1 < len(s)
                and s[i] in subtractIfNext
                and s[i + 1] in subtractIfNext[s[i]]
            ):
                multiplier = -1
            res += dictionary[s[i]] * multiplier
        return res