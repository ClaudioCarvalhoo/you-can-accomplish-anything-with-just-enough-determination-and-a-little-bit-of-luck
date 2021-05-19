# Minimum Passes Of Matrix

# O(n*m)
# n = len(matrix) | m = len(matrix[0])

from collections import deque

def minimumPassesOfMatrix(matrix):
    visited = [[False for _ in range(len(matrix[i]))] for i in range(len(matrix))]
	numVisited = 0
	visitGoal = 0
	queue = deque()
	for y in range(len(matrix)):
		for x in range(len(matrix[y])):
			visitGoal += 1
			if matrix[y][x] >= 0:
				visited[y][x] = True
				numVisited += 1
				if matrix[y][x] > 0:
					queue.append((y, x, 0))
	
	passes = 0
	while len(queue) > 0:
		elem = queue.popleft()
		passes = elem[2]
		neighbors = getUnvisitedNeighbors(elem[0], elem[1], visited)
		for neighbor in neighbors:
			visited[neighbor[0]][neighbor[1]] = True
			numVisited += 1
			queue.append((neighbor[0], neighbor[1], elem[2]+1))
	
	return passes if numVisited >= visitGoal else -1
		
		
def getUnvisitedNeighbors(y, x, visited):
	res = []
	if y-1 >= 0 and not visited[y-1][x]:
		res.append((y-1, x))
	if x-1 >= 0 and not visited[y][x-1]:
		res.append((y, x-1))
	if y+1 < len(visited) and not visited[y+1][x]:
		res.append((y+1, x))
	if x+1 < len(visited[y]) and not visited[y][x+1]:
		res.append((y, x+1))
	return res
