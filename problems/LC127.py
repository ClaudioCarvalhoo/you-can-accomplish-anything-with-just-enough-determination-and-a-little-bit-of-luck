# O(n²*m)
# n = len(wordList) | m = len(beginWord)

from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordToGenericTransformations = {}
        genericTransformationToWords = {}
        wordList.append(beginWord)
        for word in wordList:
            wordToGenericTransformations[word] = self.buildGenericTransformations(
                word, genericTransformationToWords
            )

        visited = set([beginWord])
        queue = deque([(beginWord, 1)])
        while len(queue) > 0:
            word, pathSize = queue.popleft()
            if word == endWord:
                return pathSize
            for genericTransformation in wordToGenericTransformations[word]:
                for adjWord in genericTransformationToWords[genericTransformation]:
                    if adjWord not in visited:
                        visited.add(adjWord)
                        queue.append((adjWord, pathSize + 1))
        return 0

    def buildGenericTransformations(self, word, genericTransformationToWords):
        res = set()
        for i in range(len(word)):
            genericTransformation = word[:i] + "-" + word[i + 1 :]
            res.add(genericTransformation)
            if genericTransformation not in genericTransformationToWords:
                genericTransformationToWords[genericTransformation] = set()
            genericTransformationToWords[genericTransformation].add(word)
        return res