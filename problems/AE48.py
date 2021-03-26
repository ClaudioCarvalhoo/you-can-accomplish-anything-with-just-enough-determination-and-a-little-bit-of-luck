# Single Cycle Check

# O(n)
# n = len(array)

import random

def hasSingleCycle(array):
    visited = [False for _ in array]
	numberOfVisiteds = 0
	
	initial = random.randrange(0, len(array)) # Just for fun, might as well be 0 or len(array)-1
	i = initial
	while True:
		if visited[i]:
			if numberOfVisiteds == len(array) and i == initial:
				return True
			else:
				return False
		else:
			visited[i] = True
			numberOfVisiteds += 1
			i = (i + array[i]) % len(array)
