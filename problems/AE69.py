# Longest Palindromic Substring

# O(n²)
# n = len(string)

def longestPalindromicSubstring(string):
    best = [0, 0]
	for i in range(len(string)):
		centerPalindrome = expand(string, i, i)
		leftPalindrome = expand(string, i-1, i)
		if centerPalindrome and centerPalindrome[1]-centerPalindrome[0] > best[1]-best[0]:
			best = centerPalindrome
		if leftPalindrome and leftPalindrome[1]-leftPalindrome[0] > best[1]-best[0]:
			best = leftPalindrome
	return string[best[0]:best[1]+1]

def expand(string, start, end):
	if start < 0 or end >= len(string) or string[start] != string[end]:
		return None
	while start-1 >= 0 and end+1 < len(string) and string[start-1] == string[end+1]:
		start -= 1
		end += 1
	return [start, end]