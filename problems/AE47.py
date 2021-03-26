# Kadane's Algorithm

# O(n)
# n = len(array)

def kadanesAlgorithm(array):
    indexOfFirstPositive = 0
	while array[indexOfFirstPositive] <= 0:
		indexOfFirstPositive += 1
		if indexOfFirstPositive >= len(array):
			return max(array)
	
	res = float('-inf')
	currentSum = 0
	for num in array[indexOfFirstPositive:]:
		if currentSum + num >= 0:
			currentSum += num
		else:
			currentSum = 0
		res = max(currentSum, res)
		
	return res