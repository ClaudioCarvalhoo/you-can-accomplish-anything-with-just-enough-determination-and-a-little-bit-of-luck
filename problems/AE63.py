# Staircase Traversal

# O(n)
# n = len(height)

def staircaseTraversal(height, maxSteps):
    ways = [0 for _ in range(height+1)]
	ways[0] = 1
	
	window = 1
	amountInWindow = 1
	for i in range(1, height+1):
		ways[i] = window
		window += ways[i]
		if amountInWindow < maxSteps:
			amountInWindow += 1
		else:
			window -= ways[i-maxSteps]
	return ways[-1]