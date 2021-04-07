# O(n)
# n = len(source)

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        isInMultiline = False
        cleanLine = []
        for line in source:
            used = set()
            for i in range(len(line)):
                if not isInMultiline:
                    if line[i] == "/" and i+1 < len(line):
                        if line[i+1] == "/":
                            break
                        if line[i+1] == "*":
                            isInMultiline = True
                            used.add(i+1)
                        else:
                            cleanLine.append(line[i])
                    else:
                        cleanLine.append(line[i])
                elif i > 0 and line[i] == "/" and line[i-1] == "*" and i-1 not in used:
                    isInMultiline = False
            if len(cleanLine) > 0 and not isInMultiline:
                res.append(''.join(cleanLine))
                cleanLine = []
        return res
