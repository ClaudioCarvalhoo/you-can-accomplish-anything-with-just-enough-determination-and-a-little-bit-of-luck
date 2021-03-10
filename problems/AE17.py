# Bubble Sort

# O(n²)
# n = len(array)

def bubbleSort(array):
    for i in range(len(array)):
		for j in range(i+1, len(array)):
			if array[j] < array[i]:
				temp = array[j]
				array[j] = array[i]
				array[i] = temp
	return array
