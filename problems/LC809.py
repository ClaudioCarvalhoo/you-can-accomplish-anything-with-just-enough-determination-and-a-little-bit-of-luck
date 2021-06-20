# O(k+(n*m))
# k = len(s) | n = len(words) | m = maxLen(words)


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        target = self.parseWord(s)
        res = 0
        for word in words:
            if self.isStretchy(word, target):
                res += 1
        return res

    def parseWord(self, s):
        if len(s) == 0:
            return []

        res = []
        curChar = s[0]
        curCount = 0
        for char in s:
            if char == curChar:
                curCount += 1
            else:
                res.append((curChar, curCount))
                curChar = char
                curCount = 1
        res.append((curChar, curCount))
        return res

    def isStretchy(self, word, target):
        word = self.parseWord(word)
        if len(word) != len(target):
            return False
        for i in range(len(word)):
            if (
                word[i][0] != target[i][0]
                or word[i][1] > target[i][1]
                or (word[i][1] != target[i][1] and target[i][1] < 3)
            ):
                return False
        return True
