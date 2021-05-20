# Longest Substring Without Duplication

# O(n)
# n = len(string)

def longestSubstringWithoutDuplication(string):
	if len(string) <= 0:
		return ""
	
	best = (0, 0)
    counter = {}
	start = 0
	inWindow = set()
	for i in range(len(string)):
		char = string[i]
		while char in inWindow:
			removed = string[start]
			counter[removed] -= 1
			if counter[removed] == 0:
				inWindow.remove(removed)
			start += 1
		if char in counter:
			counter[char] += 1
		else:
			counter[char] = 1
		inWindow.add(char)
		if i - start > best[1] - best[0]:
			best = (start, i)
		
	return string[best[0]:best[1]+1]
