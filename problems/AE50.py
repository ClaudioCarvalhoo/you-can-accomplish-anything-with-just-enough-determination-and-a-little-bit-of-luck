# River Sizes

# O(n*m)
# n = len(matrix) | m = len(matrix[0])

def riverSizes(matrix):
	riverSizes = []
    visited = [[False for _ in matrix[0]] for _ in matrix]
	for y in range(len(matrix)):
		for x in range(len(matrix[y])):
			if not visited[y][x] and matrix[y][x] == 1:
				riverSizes.append(exploreRiver(matrix, visited, y ,x))
			visited[y][x] = True
	return riverSizes

def exploreRiver(matrix, visited, y, x):
	if y < 0 or y >= len(matrix) or x < 0 or x >= len(matrix[y]) or visited[y][x] or matrix[y][x] != 1:
		return 0
	
	visited[y][x] = True
	riverSize = 0
	riverSize += exploreRiver(matrix, visited, y-1, x)
	riverSize += exploreRiver(matrix, visited, y, x+1)
	riverSize += exploreRiver(matrix, visited, y+1, x)
	riverSize += exploreRiver(matrix, visited, y, x-1)
	return riverSize + 1