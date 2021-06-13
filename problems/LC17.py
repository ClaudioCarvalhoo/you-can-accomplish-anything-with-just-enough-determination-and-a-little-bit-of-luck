# O(n*4ⁿ)
# n = len(digits)


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        numberToLetters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        res = []
        self.explore(digits, numberToLetters, 0, [], res)
        return res

    def explore(self, digits, numberToLetters, i, cur, res):
        if i >= len(digits):
            res.append("".join(cur))
        else:
            for letter in numberToLetters[digits[i]]:
                cur.append(letter)
                self.explore(digits, numberToLetters, i + 1, cur, res)
                cur.pop()