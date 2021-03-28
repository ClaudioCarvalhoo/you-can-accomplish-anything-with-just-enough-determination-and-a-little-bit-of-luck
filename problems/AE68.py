# Sunset Views

# O(n)
# n = len(buildings)

def sunsetViews(buildings, direction):
    scanRange = range(len(buildings))
	if direction == 'EAST':
		scanRange = range(len(buildings)-1, -1, -1)
	
	res = []
	tallestSoFar = 0
	for i in scanRange:
		if buildings[i] > tallestSoFar:
			res.append(i)
			tallestSoFar = buildings[i]
	
	if direction == 'EAST':
		res = list(reversed(res))
	return res
