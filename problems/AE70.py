# Group Anagrams

# O(n*w*log(w))
# n = len(words) | w = len(largestString(words))

def groupAnagrams(words):
    normalizedWords = [''.join(sorted(word)) for word in words]
	positions = {}
	res = []
	for i in range(len(words)):
		if normalizedWords[i] in positions:
			res[positions[normalizedWords[i]]].append(words[i])
		else:
			res.append([words[i]])
			positions[normalizedWords[i]] = len(res)-1
	return res
