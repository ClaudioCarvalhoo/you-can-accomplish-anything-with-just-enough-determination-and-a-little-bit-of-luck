# O(n*m)
# n = len(words) | m = len(maxWidth)


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        while i < len(words):
            newLine, i = self.createLine(words, i, maxWidth)
            res.append(newLine)
        return res

    def createLine(self, words, start, maxWidth):
        end = start
        charCount = len(words[start])
        while end + 1 < len(words) and charCount + 1 + len(words[end + 1]) <= maxWidth:
            end += 1
            charCount += 1 + len(words[end])

        newLine = ""
        if start == end or end == len(words) - 1:
            newLine = self.createLeftJustifiedLine(words, start, end, maxWidth)
        else:
            newLine = self.createFullyJustifiedLine(words, start, end, maxWidth)
        return newLine, end + 1

    def createLeftJustifiedLine(self, words, start, end, maxWidth):
        newLine = []
        newLineLength = 0
        for i in range(start, end + 1):
            newLine.append(words[i])
            newLineLength += len(words[i])
            if i != end:
                newLine.append(" ")
                newLineLength += 1
        newLine += [" "] * (maxWidth - newLineLength)
        return "".join(newLine)

    def createFullyJustifiedLine(self, words, start, end, maxWidth):
        newLine = []
        newLineRawLength = 0
        for i in range(start, end + 1):
            newLineRawLength += len(words[i])
        necessarySpaces = maxWidth - newLineRawLength
        spacesBetweenWords = necessarySpaces // (end - start)
        remainingSpaces = necessarySpaces % (end - start)
        for i in range(start, end + 1):
            newLine.append(words[i])
            if i != end:
                newLine += [" "] * spacesBetweenWords
                if remainingSpaces > 0:
                    newLine.append(" ")
                    remainingSpaces -= 1
        return "".join(newLine)
