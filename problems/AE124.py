# Underscorify Substring

# O(n)
# n = len(string)

def underscorifySubstring(string, substring):
	building = 0
	ranges1 = []
    for i in range(len(string)):
		if string[i] == substring[building]:
			building += 1
		else:
			building = 0
		if building == len(substring):
			ranges1.append((i-len(substring)+1, i))
			building = 0
			if len(substring) > 1 and string[i] == substring[building]:
				building += 1
	
	reverseRanges = []
	for i in range(len(string)-1, -1, -1):
		if string[i] == substring[-building-1]:
			building += 1
		else:
			building = 0
		if building == len(substring):
			reverseRanges.append((i, i+len(substring)-1))
			building = 0
			if len(substring) > 1 and string[i] == substring[-building-1]:
				building += 1
	ranges2 = list(reversed(reverseRanges))
	
			
	i1 = 0
	i2 = 0
	underscorePositions = []
	while i1 < len(ranges1) or i2 < len(ranges2):
		range1 = getRange(ranges1, i1)
		range2 = getRange(ranges2, i2)
		if range1[0] <= range2[0]:
			start = range1[0]
			end = range1[1]
		else:
			start = range2[0]
			end = range2[1]+1
		while range1[0] <= end or range2[0] <= end:
			range1 = getRange(ranges1, i1)
			range2 = getRange(ranges2, i2)
			if range1[0] <= end:
				end = max(end, range1[1]+1)
				i1 += 1
			if range2[0] <= end:
				end = max(end, range2[1]+1)
				i2 += 1
		underscorePositions += [start, end]
		
	res = []
	underscoreIndex = 0
	for i in range(len(string)):
		if underscoreIndex < len(underscorePositions) and underscorePositions[underscoreIndex] == i:
			res.append('_')
			underscoreIndex += 1
		res.append(string[i])
	if underscoreIndex < len(underscorePositions) and underscorePositions[underscoreIndex] == len(string):
			res.append('_')
	
	return ''.join(res)
				
	
def getRange(ranges, i):
	if i < len(ranges):
		return ranges[i]
	else:
		return (float('inf'), float('-inf'))
		
		
