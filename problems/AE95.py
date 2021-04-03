# Maximum Sum Submatrix

# O(n*m)
# n = len(matrix) | m = len(matrix[0])

def maximumSumSubmatrix(matrix, size):
    sums = [[val for val in row] for row in matrix]
	for y in range(len(sums)):
		for x in range(len(sums[y])):
			if x > 0:
				sums[y][x] += sums[y][x-1]
			if y > 0:
				sums[y][x] += sums[y-1][x]
			if x > 0 and y > 0:
				sums[y][x] -= sums[y-1][x-1]
				
	res = float("-inf")
	for y in range(size-1, len(matrix)):
		for x in range(size-1, len(matrix[y])):
			total = sums[y][x]
			subtractY = y-size
			subtractX = x-size
			total -= getValueToSubtract(sums, subtractY, x) + getValueToSubtract(sums, y, subtractX) - getValueToSubtract(sums, subtractY, subtractX)
			res = max(res, total)
	return res
			
def getValueToSubtract(sums, y, x):
	if y < 0 or x < 0:
		return 0
	else:
		return sums[y][x]