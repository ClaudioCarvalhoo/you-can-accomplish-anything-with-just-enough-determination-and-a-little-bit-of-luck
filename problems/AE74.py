# Four Number Sum

# Actually O(n²) in average case
# n = len(array)

def fourNumberSum(array, targetSum):
    res = []
	pairsSum = {}
	for i in range(len(array)):
		for j in range(i+1, len(array)):
			pair = [array[i], array[j]]
			complement = targetSum - sum(pair)
			if complement in pairsSum:
				for complementaryPair in pairsSum[complement]:
					res.append(pair + complementaryPair)
		for j in range(i-1, -1, -1):
			pair = [array[i], array[j]]
			if sum(pair) in pairsSum:
				pairsSum[sum(pair)].append(pair)
			else:
				pairsSum[sum(pair)] = [pair]			
	return res
