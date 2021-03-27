# Search In Sorted Matrix

# O(n+m)
# n = len(matrix) | m = len(matrix[0])

def searchInSortedMatrix(matrix, target):
    y = 0
	x = len(matrix[0])-1
	while y < len(matrix) and x >= 0:
		if matrix[y][x] == target:
			return [y, x]
		elif matrix[y][x] > target:
			x -= 1
		else:
			y += 1
		
	return [-1, -1]
