# Maximize Expression

# O(n)
# n = len(array)

def maximizeExpression(array):
    if len(array) < 4:
		return 0
	
	bestA = []
	for i in range(len(array)):
		if i-1 >= 0:
			bestA.append(max(bestA[i-1], array[i]))
		else:
			bestA.append(array[i])
	
	bestAB = []
	for i in range(len(array)):
		if i-1 >= 0:
			bestAB.append(max(bestAB[i-1], bestA[i-1]-array[i]))
		else:
			bestAB.append(float('-inf'))
	
	bestABC = []
	for i in range(len(array)):
		if i-2 >= 0:
			bestABC.append(max(bestABC[i-1], bestAB[i-1]+array[i]))
		else:
			bestABC.append(float('-inf'))
			
	bestABCD = []
	for i in range(len(array)):
		if i-3 >= 0:
			bestABCD.append(max(bestABCD[i-1], bestABC[i-1]-array[i]))
		else:
			bestABCD.append(float('-inf'))
	
	return bestABCD[-1]
