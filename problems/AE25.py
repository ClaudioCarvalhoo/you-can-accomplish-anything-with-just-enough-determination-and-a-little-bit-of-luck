# Smallest Difference

# O(n*log(n) + m*log(m))
# n = len(arrayOne) | m = len(arrayTwo)

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
	arrayTwo.sort()
	indexOne = 0
	indexTwo = 0
	res = [0, 0]
	while indexOne < len(arrayOne) and indexTwo < len(arrayTwo):
		diff = absDiff(arrayOne[indexOne], arrayTwo[indexTwo])
		if diff < absDiff(arrayOne[res[0]], arrayTwo[res[1]]):
			res = [indexOne, indexTwo]
		if arrayOne[indexOne] == arrayTwo[indexTwo]:
			break
		elif arrayOne[indexOne] < arrayTwo[indexTwo]:
			indexOne += 1
		else:
			indexTwo += 1
	return [arrayOne[res[0]], arrayTwo[res[1]]]
		
		
def absDiff(a, b):
	return abs(abs(a)-abs(b))