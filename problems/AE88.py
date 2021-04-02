# Numbers In Pi

# O(n³+m)
# n = len(pi) | m = len(numbers)

def numbersInPi(pi, numbers):
    numbers = set(numbers)
	res = explore(pi, numbers, 0, 0, [None for _ in pi])
	return res if res != float('inf') else -1
			
			
def explore(pi, numbers, i, spaces, necessarySpacesAfter):
	cur = ""
	best = float('inf')
	for j in range(i, len(pi)):
		cur += pi[j]
		if cur in numbers:
			if j == len(pi)-1:
				return spaces
			spacesAfter = necessarySpacesAfter[j+1]
			if spacesAfter == None:
				spacesAfter = explore(pi, numbers, j+1, spaces+1, necessarySpacesAfter)
				necessarySpacesAfter[j+1] = spacesAfter - spaces
			best = min(best, spacesAfter)
	return best
			