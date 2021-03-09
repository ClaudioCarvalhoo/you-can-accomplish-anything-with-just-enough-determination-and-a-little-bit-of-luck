# Validate Subsequence

# O(n)
# n = len(array)

def isValidSubsequence(array, sequence):
	if len(sequence) == 0:
		return True
	
    sequenceIndex = 0
	for cur in array:
		if cur == sequence[sequenceIndex]:
			sequenceIndex += 1
		if sequenceIndex >= len(sequence):
			return True
	return False
