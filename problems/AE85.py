# Water Area

# O(n)
# n = len(heights)

# Sol 1
def waterArea(heights):
	tallestAfter = [0 for _ in heights]
	for i in range(len(heights)-2, -1, -1):
		tallestAfter[i] = max(heights[i+1], tallestAfter[i+1])
		
	res = 0
	i = 0	
	while i < len(heights)-1:
		j = i+1
		while heights[j] < heights[i] and not (tallestAfter[j] < heights[j]) and j+1 < len(heights):
			j += 1
		maxWaterLevel = min(heights[i], heights[j])
		for w in range(i+1, j):
			res += maxWaterLevel - heights[w]
		if tallestAfter[j] == 0:
			break
		i = j
	return res
		
# Sol 2
def waterArea(heights):
	tallestAfter = [0 for _ in heights]
	for i in range(len(heights)-2, -1, -1):
		tallestAfter[i] = max(heights[i+1], tallestAfter[i+1])
	tallestBefore = [0 for _ in heights]
	for i in range(1, len(heights)):
		tallestBefore[i] = max(heights[i-1], tallestBefore[i-1])
		
	res = 0
	for i in range(len(heights)):
		if tallestBefore[i] > heights[i] and tallestAfter[i] > heights[i]:
			res += min(tallestBefore[i], tallestAfter[i]) - heights[i]
	return res
		
# Sol 3
def waterArea(heights):
	if len(heights) == 0:
		return 0
	res = 0
	
    leftBound = heights[0]
	rightBound = heights[-1]
	leftIndex = 0
	rightIndex = len(heights)-1
	while leftIndex < rightIndex:
		if heights[leftIndex] < heights[rightIndex]:
			leftIndex += 1
			leftBound = max(leftBound, heights[leftIndex])
			res += leftBound - heights[leftIndex]
		else:
			rightIndex -= 1
			rightBound = max(rightBound, heights[rightIndex])
			res += rightBound - heights[rightIndex]
	return res
