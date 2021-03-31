# Same BSTs

# O(n²)
# n = len(arrayOne)

def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) != len(arrayTwo):
		return False
	
	for i in range(len(arrayOne)):
		num = arrayOne[i]
		previousAppearances = getNumberOfPreviousAppearancesUpTo(arrayOne, i, num)
		pathOne = calculatePathTo(arrayOne, num, previousAppearances)
		pathTwo = calculatePathTo(arrayTwo, num, previousAppearances)
		if pathTwo == None or len(pathOne) != len(pathTwo):
			return False
		for i in range(len(pathOne)):
			if pathOne[i] != pathTwo[i]:
				return False
	return True
		
def calculatePathTo(array, num, previousAppearances):
	path = []
	upperBound = float('inf')
	lowerBound = float('-inf')
	for i in range(len(array)):
		cur = array[i]
		if cur == num:
			if previousAppearances == 0:
				return path
			else:
				previousAppearances -= 1
		if cur > lowerBound and cur <= upperBound:
			path.append(cur)
			if num >= cur:
				lowerBound = cur
			else:
				upperBound = cur
	return None

def getNumberOfPreviousAppearancesUpTo(array, i, num):
	previousAppearances = 0
	for x in range(i):
		if array[x] == num:
			previousAppearances += 1
	return previousAppearances