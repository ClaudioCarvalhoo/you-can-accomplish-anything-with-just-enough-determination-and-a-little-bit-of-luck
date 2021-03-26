# Remove Islands

# O(m*n)
# m = len(matrix) | n = len(matrix[0])

def removeIslands(matrix):
	visited = [[False for _ in matrix[0]] for _ in matrix]
    for y in range(1, len(matrix)-1):
		for x in range(1, len(matrix[y])-1):
			if not visited[y][x] and matrix[y][x] == 1 and isIsland(matrix, visited, y, x):
				removeIsland(matrix, y, x)
			visited[y][x] = True
	return matrix
			
def isIsland(matrix, visited, y, x):
	if visited[y][x] or matrix[y][x] == 0:
		return True
	
	if y == 0 or y == len(matrix)-1 or x == 0 or x == len(matrix[y])-1:
		return False
	
	visited[y][x] = True
	return isIsland(matrix, visited, y-1, x) and isIsland(matrix, visited, y+1, x) and isIsland(matrix, visited, y, x-1) and isIsland(matrix, visited, y, x+1)

def removeIsland(matrix, y, x):
	if matrix[y][x] == 1:
		matrix[y][x] = 0
		removeIsland(matrix, y-1, x)
		removeIsland(matrix, y+1, x)
		removeIsland(matrix, y, x-1)
		removeIsland(matrix, y, x+1)
	
