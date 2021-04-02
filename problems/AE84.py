# Min Number Of Jumps

# O(n)
# n = len(array)

# Sol 1
def minNumberOfJumps(array):
    necessary = [0]
	for i in range(len(array)):
		j = i + array[i]
		for k in range(len(necessary), min(j+1, len(array))):
			necessary.append(necessary[i]+1)
	return necessary[-1]


# Sol 2
def minNumberOfJumps(array):
    reachable = 0
	previouslyReachable = 0
	jumps = 0
	for i in range(len(array)-1):
		reachable = max(reachable, i+array[i])
		if previouslyReachable <= i:
			jumps += 1
			previouslyReachable = max(previouslyReachable, reachable)
	return jumps
		