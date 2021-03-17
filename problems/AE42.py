# Max Subset Sum No Adjacent

# O(n)
# n = len(array)

def maxSubsetSumNoAdjacent(array):
    if len(array) <= 0:
		return 0
	
	bestSoFar = {'non-adjacent': array[0], 'adjacent': 0}
	for i in range(1, len(array)):
		bestPossibleValue = max(array[i] + bestSoFar['adjacent'], bestSoFar['non-adjacent'])
		bestSoFar['adjacent'] = bestSoFar['non-adjacent']
		bestSoFar['non-adjacent'] = bestPossibleValue
	return bestSoFar['non-adjacent']
	