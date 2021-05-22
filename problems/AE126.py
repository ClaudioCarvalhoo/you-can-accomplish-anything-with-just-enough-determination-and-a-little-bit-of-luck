# Multi String Search

# O(n*k + m*k)
# n = len(bigString) | m = len(smallStrings) | k = maxLen(smallStrings)

def multiStringSearch(bigString, smallStrings):
    trie = buildTrie(smallStrings)
	res = {}
	for i in range(len(bigString)):
		match(bigString, trie, i, res)
	return [string in res for string in smallStrings]
	
	
def buildTrie(smallStrings):
	trie = {}
	for string in smallStrings:
		cur = trie
		for char in string:
			if char not in cur:
				cur[char] = {}
			cur = cur[char]
		cur[True] = string
	return trie


def match(bigString, trie, start, res):
	i = start
	while i < len(bigString) and bigString[i] in trie:
		if True in trie:
			res[trie[True]] = True
		trie = trie[bigString[i]]
		i += 1
	if True in trie:
		res[trie[True]] = True