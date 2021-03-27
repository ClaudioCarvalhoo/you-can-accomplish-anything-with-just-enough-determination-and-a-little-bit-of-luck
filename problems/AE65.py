# Three Number Sort

# O(n)
# n = len(array)

def threeNumberSort(array, order):
    cur = 0
	for number in order:
		for i in range(len(array)):
			if array[i] == number:
				swap(array, cur, i)
				cur += 1
	return array
	
def swap(array, i, j):
	array[i], array[j] = array[j], array[i]