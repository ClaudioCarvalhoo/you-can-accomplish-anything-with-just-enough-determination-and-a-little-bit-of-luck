# O(n*d)
# n = len(s) | d = len(dictionary)


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        res = ""
        words = set(dictionary)
        currents = {word: 0 for word in words}
        for stringChar in s:
            toRemove = []
            for word in words:
                if word[currents[word]] == stringChar:
                    currents[word] += 1
                if currents[word] == len(word):
                    if len(word) > len(res) or (len(word) == len(res) and word < res):
                        res = word
                    toRemove.append(word)
            for word in toRemove:
                words.remove(word)
        return res