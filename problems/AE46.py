# Number Of Ways To Traverse Graph

# O(n*m)
# n = len(width) | m = len(height)

def numberOfWaysToTraverseGraph(width, height):
    res = [[0 for _ in range(width)] for _ in range(height)]
	res[0][0] = 1
	
	for y in range(height):
		for x in range(width):
			if y > 0:
				res[y][x] += res[y-1][x]
			if x > 0:
				res[y][x] += res[y][x-1]
	
	return res[-1][-1]