# Disk Stacking

# O(n²)
# n = len(disks)

# Sol 1
def diskStacking(disks):
    tallestWithBottom = [[] for disk in disks]
	
	for i in range(len(disks)):
		if tallestWithBottom[i] == []:
			explore(disks, tallestWithBottom, i)
		
	tallestStack = []
	tallestStackHeight = 0
	for stack in tallestWithBottom:
		stackHeight = 0
		for disk in stack:
			stackHeight += disk[2]
		if stackHeight > tallestStackHeight:
			tallestStack = stack
			tallestStackHeight = stackHeight
	return tallestStack
			
def explore(disks, tallestWithBottom, i):
	if tallestWithBottom[i] != []:
		return tallestWithBottom[i]
	
	bestOnTop = []
	for j in range(len(disks)):
		if j == i:
			continue
		if canGoOnTop(disks[i], disks[j]):
			tallestWithJOnTop = explore(disks, tallestWithBottom, j)
			bestOnTop = max(bestOnTop, tallestWithJOnTop, key=len)
	tallestWithBottom[i] = [disks[i]] + bestOnTop
	return tallestWithBottom[i]

def canGoOnTop(bottomDisk, topDisk):
	return topDisk[0] > bottomDisk[0] and topDisk[1] > bottomDisk[1] and topDisk[2] > bottomDisk[2]

# Sol 2
def diskStacking(disks):
    disks.sort(key=lambda x: x[2])
	bestHeightStartingAt = [disk[2] for disk in disks]
	putOnTop = [None for _ in disks]
	for i in range(len(disks)):
		curDisk = disks[i]
		for j in range(i):
			if canGoOnTop(disks[j], curDisk) and curDisk[2] + bestHeightStartingAt[j] > bestHeightStartingAt[i]:
				bestHeightStartingAt[i] = curDisk[2] + bestHeightStartingAt[j]
				putOnTop[i] = j
				
	bestBottom = 0
	for i in range(len(bestHeightStartingAt)):
		if bestHeightStartingAt[i] > bestHeightStartingAt[bestBottom]:
			bestBottom = i
			
	res = []
	i = bestBottom
	while i is not None:
		res.append(i)
		i = putOnTop[i]
	print(res)
	res = list(reversed([disks[i] for i in res]))
	return res
	
def canGoOnTop(bottomDisk, topDisk):
	return topDisk[0] > bottomDisk[0] and topDisk[1] > bottomDisk[1] and topDisk[2] > bottomDisk[2]