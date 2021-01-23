from typing import List


class Solution:
    def findReplaceString(
        self, S: str, indexes: List[int], sources: List[str], targets: List[str]
    ) -> str:
        res = ""

        alteredIndexes = {}

        for i in range(len(indexes)):
            initialIndex = indexes[i]
            ok = True
            for j in range(len(sources[i])):
                if initialIndex + j >= len(S) or S[initialIndex + j] != sources[i][j]:
                    ok = False
                    break
            if ok:
                alteredIndexes[initialIndex] = targets[i]
                for k in range(1, len(sources[i])):
                    alteredIndexes[initialIndex + k] = ""

        for x in range(len(S)):
            if x in alteredIndexes:
                res += alteredIndexes[x]
            else:
                res += S[x]

        return res