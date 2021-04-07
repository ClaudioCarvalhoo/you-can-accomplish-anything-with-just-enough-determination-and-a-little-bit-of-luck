 # Quick Sort
  
 # O(n*log(n)) average case
 # n = len(array)

def quickSort(array):
    helper(array, 0, len(array)-1)
	return array
	
def helper(array, start, end):
	if start == end or start > end:
		return
	pivot = end
	i = start
	for j in range(start, pivot):
		if array[j] < array[pivot]:
			swap(array, i, j)
			i += 1
	swap(array, i, pivot)
	helper(array, start, i-1)
	helper(array, i+1, end)
		
def swap(array, i, j):
	array[i], array[j] = array[j], array[i]
