class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = {}
        for word in wordDict:
            curTrieLevel = trie
            for char in word:
                if char not in curTrieLevel:
                    curTrieLevel[char] = {}
                curTrieLevel = curTrieLevel[char]
            curTrieLevel[True] = True

        res = set()
        self.explore(s, trie, trie, [], 0, res)
        return list(res)

    def explore(self, s, trie, curTrieLevel, sentence, index, res):
        if index >= len(s):
            if True in curTrieLevel:
                res.add("".join(sentence).rstrip())
            return
        if s[index] not in curTrieLevel:
            return
        if True in curTrieLevel[s[index]]:
            self.explore(s, trie, trie, sentence + [s[index], " "], index + 1, res)
        self.explore(
            s, trie, curTrieLevel[s[index]], sentence + [s[index]], index + 1, res
        )
