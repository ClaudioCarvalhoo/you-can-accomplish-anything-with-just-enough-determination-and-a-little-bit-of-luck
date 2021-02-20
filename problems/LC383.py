# O(n + m)
# n = len(ransomNote) | m = len(magazine)


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = {}
        for letter in magazine:
            if letter in counter:
                counter[letter] += 1
            else:
                counter[letter] = 1

        for letter in ransomNote:
            if not letter in counter or counter[letter] <= 0:
                return False
            else:
                counter[letter] -= 1

        return True