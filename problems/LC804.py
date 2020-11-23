# O(n * m)
# n = len(words) | m = len(words[largestWord])


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        transformations = set()
        letters = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        for word in words:
            res = ""
            for letter in word:
                res += letters[ord(letter) - 97]
            transformations.add(res)
        return len(transformations)