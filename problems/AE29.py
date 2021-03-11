# Longest Peak

# O(n)
# n = len(array)

# Sol 1
def longestPeak(array):
	best = 0
	i = 1
    while i < len(array)-1:
		
		# Find first increasing sequence
		while i < len(array) and array[i] <= array[i-1]:
			i += 1
		current = 1
				
		# Climb to top
		while i < len(array) and array[i] > array[i-1]:
			current += 1
			i += 1
		
		# If plateau, disregard
		if i >= len(array) or array[i] == array[i-1]:
			continue
		
		# Go downhill
		while i < len(array) and array[i] < array[i-1]:
			current += 1
			i += 1
		
		# If peak was found, compare it to previous best
		if current >= 3:
			best = max(best, current)
				
	return best

# Sol 2
def longestPeak(array):
    peaks = []
	for i in range(1, len(array)-1):
		if array[i-1] < array[i] and array[i+1] < array[i]:
			peaks.append(i)
			
	best = 0
	for peak in peaks:
		right = 0
		i = peak-1
		while i >= 0 and array[i] < array[i+1]:
			right += 1
			i -= 1
			
		left = 0
		i = peak+1
		while i < len(array) and array[i] < array[i-1]:
			left += 1
			i += 1
			
		best = max(best, left+right+1)
	return best

# Sol 3 (With O(1) space)
def longestPeak(array):
	best = 0
	for i in range(1, len(array)-1):
		if array[i-1] < array[i] and array[i+1] < array[i]:
			best = max(best, getPeakLength(array, i))
	return best

def getPeakLength(array, peak):
	right = 0
	i = peak-1
	while i >= 0 and array[i] < array[i+1]:
		right += 1
		i -= 1

	left = 0
	i = peak+1
	while i < len(array) and array[i] < array[i-1]:
		left += 1
		i += 1
	return left+right+1