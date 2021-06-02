# O(n*k + m)
# n = len(products) | k = maxLen(products) | m = len(searchWord)


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        trie = self.buildTrie(products)
        res = []
        for char in searchWord:
            if char not in trie:
                trie = {}
                res.append([])
            else:
                trie = trie[char]
                res.append(trie["matches"])
        return res

    def buildTrie(self, words):
        trieRoot = {}
        for word in words:
            curNode = trieRoot
            for char in word:
                if char not in curNode:
                    curNode[char] = {}
                curNode = curNode[char]
                self.insertWordInNodeMatches(word, curNode)
            curNode[True] = True
        return trieRoot

    def insertWordInNodeMatches(self, word, curNode):
        if "matches" not in curNode:
            curNode["matches"] = []
        curNode["matches"].append(word)
        curNode["matches"].sort()
        if len(curNode["matches"]) > 3:
            curNode["matches"].pop()
