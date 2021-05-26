# O(n*k)
# n = len(strings) | k = maxLen(strings)


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        resDict = {}
        for string in strings:
            combination = []
            for i in range(1, len(string)):
                combination.append(self.getDistance(string[i - 1], string[i]))
            combination = tuple(combination)
            if combination in resDict:
                resDict[combination].append(string)
            else:
                resDict[combination] = [string]
        return resDict.values()

    def getDistance(self, a, b):
        return (ord(b) - ord(a)) % 26
