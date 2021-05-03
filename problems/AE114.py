# Quickselect

def quickselect(array, k):
	target = k-1
	
	start = 0
    pivotIndex = len(array)-1
	while True:
		i = start
		for j in range(start, pivotIndex):
			if array[j] < array[pivotIndex]:
				swap(array, i, j)
				i += 1
		swap(array, i, pivotIndex)
		if i == target:
			return array[target]
		if i > target:
			pivotIndex = i-1
		if i < target:
			start = i+1
		
	
def swap(array, i, j):
	array[i], array[j] = array[j], array[i]
