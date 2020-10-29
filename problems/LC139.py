# O(n*d*w)
# n=len(s) | d=len(wordDict) | w=len(wordDict[x])
# Could be optimized by using a trie instead of comparing strings

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        possible = {0: True}

        for i in range(len(s)):
            if i in possible:
                for word in wordDict:
                    if s[i : i + len(word)] == word:
                        possible[i + len(word)] = True

        if len(s) in possible:
            return True
        else:
            return False