# Binary Search

# O(log(n))
# n = len(array)

def binarySearch(array, target):
    left = 0
	right = len(array)-1
	
	while left <= right:
		midpoint = left + ((right-left)//2)
		if array[midpoint] == target:
			return midpoint
		elif array[midpoint] < target:
			left = midpoint+1
		else:
			right = midpoint-1
			
	return -1
