# Zigzag Traverse

# O(n*m)
# n = len(array) | m = len(array[0])

def zigzagTraverse(array):
	if(len(array) == 1):
		return array[0]
	
	y = 0
    x = 0
	res = []
	while len(res) < len(array) * len(array[0]):
		res.append(array[y][x])
		while x-1 >= 0 and y+1 < len(array):
			x -= 1
			y += 1
			res.append(array[y][x])
		if y < len(array)-1:
			y += 1
		else:
			x += 1
		
		if len(res) >= len(array) * len(array[0]):
			break
			
		res.append(array[y][x])
		while x+1 < len(array[0]) and y-1 >= 0:
			x += 1
			y -= 1
			res.append(array[y][x])
		if x < len(array[0])-1:
			x += 1
		else:
			y += 1
	return res