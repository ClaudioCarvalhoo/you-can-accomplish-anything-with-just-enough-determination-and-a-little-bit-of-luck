# Suffix Trie Construction

# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    # O(n²)
    def populateSuffixTrieFrom(self, string):
		for i in range(len(string)):
			subTrie = self.root
			for j in range(i, len(string)):
				char = string[j]
				if char not in subTrie:
					subTrie[char] = {}
				subTrie = subTrie[char]
			subTrie[self.endSymbol] = True
					
	# O(n)	
    def contains(self, string):
		subTrie = self.root
		for char in string:
			if char in subTrie:
				subTrie = subTrie[char]
			else:
				return False
		return self.endSymbol in subTrie
        
