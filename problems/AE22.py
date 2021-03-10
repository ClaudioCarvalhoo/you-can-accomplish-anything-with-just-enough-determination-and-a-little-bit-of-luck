# Run-Length Encoding

# O(n)
# n = len(string)

def runLengthEncoding(string):
	currentChar = None
	currentCount = 0
	res = []
    for char in string:
		if char == currentChar:
			currentCount += 1
		else:
			insertRepetitions(res, currentChar, currentCount)
			currentCount = 1
			currentChar = char
	insertRepetitions(res, currentChar, currentCount)
	return ''.join(res)

def insertRepetitions(res, currentChar, currentCount):
	repetitions = currentCount // 9
	rest = currentCount % 9
	res += ['9', currentChar] * repetitions
	if rest > 0:
		res += [str(rest), currentChar]