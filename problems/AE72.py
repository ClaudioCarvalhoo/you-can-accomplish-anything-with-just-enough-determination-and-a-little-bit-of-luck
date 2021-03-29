# Reverse Words In String

# O(n)
# n = len(string)

def reverseWordsInString(string):
    words = [[]]
	for char in string:
		if char == " ":
			words += [[" "], []]
		else:
			words[-1].append(char)
			
	res = []
	for i in range(len(words)-1, -1, -1):
		for char in words[i]:
			res.append(char)
	return ''.join(res)
