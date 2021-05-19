# Minimum Characters For Words

# O(n*l)
# n = len(words) | l = maxLen(words)

def minimumCharactersForWords(words):
    totalNeeded = {}
	for word in words:
		wordCharacters = {}
		for char in word:
			if char in wordCharacters:
				wordCharacters[char] += 1
			else:
				wordCharacters[char] = 1
		for char in wordCharacters:
			if char in totalNeeded:
				totalNeeded[char] = max(totalNeeded[char], wordCharacters[char])
			else:
				totalNeeded[char] = wordCharacters[char]
				
	res = []
	for char in totalNeeded:
		res += [char] * totalNeeded[char]
	return res