# First Non-Repeating Character

# O(n)
# n = len(string)

def firstNonRepeatingCharacter(string):
    counter = {}
	for letter in string:
		if letter in counter:
			counter[letter] += 1
		else:
			counter[letter] = 1
	
	for i in range(len(string)):
		if counter[string[i]] == 1:
			return i
		
	return -1
