# O(n)
# n = len(text)


class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = 0
        words = []
        for i in range(len(text)):
            if text[i] == " ":
                spaces += 1
            else:
                if i - 1 < 0 or text[i - 1] == " ":
                    words.append(text[i])
                else:
                    words[-1] += text[i]

        if len(words) == 1:
            return words[0] + (" " * spaces)

        spaces_between = int(spaces / (len(words) - 1))
        trailing_spaces = spaces % (len(words) - 1)

        res = ""
        for i in range(len(words)):
            res += words[i]
            if i < len(words) - 1:
                res += " " * spaces_between
        res += " " * trailing_spaces

        return res