# Spiral Traverse

# O(n*m)
# n = len(array) | m = len(array[0])

# Sol 1
def spiralTraverse(array):
    if len(array) == 1:
		return array[0]
	
	res = array[0]
	verticalMovement = len(array)-1
	horizontalMovement = len(array[0])-1
	verticalDirection = 1
	horizontalDirection = -1
	
	x = len(array[0])-1
	y = 0
	while verticalMovement > 0 or horizontalMovement > 0:
		tmpVertical = verticalMovement
		while tmpVertical > 0:
			y = y + verticalDirection
			res.append(array[y][x])
			tmpVertical -= 1
		verticalDirection *= -1
		verticalMovement -= 1
		if horizontalMovement <= 0:
			break
		
		tmpHorizontal = horizontalMovement
		while tmpHorizontal > 0:
			x = x + horizontalDirection
			res.append(array[y][x])
			tmpHorizontal -= 1
		horizontalDirection *= -1
		horizontalMovement -= 1
		if verticalMovement <= 0:
			break
	return res
	
# Sol 2
def spiralTraverse(array):
    startX = 0
	startY = 0
	endX = len(array[0])-1
	endY = len(array)-1
	
	res = []
	while startX <= endX and startY <= endY:
		res += array[startY][startX:endX+1]
		res += [elem[endX] for elem in array[startY+1:endY]]
		if startY != endY:
			res += reversed(array[endY][startX:endX+1])
		if startX != endX:
			res += reversed([elem[startX] for elem in array[startY+1:endY]])
		
		startX += 1
		startY += 1
		endX -= 1
		endY -= 1
		
	return res
		
