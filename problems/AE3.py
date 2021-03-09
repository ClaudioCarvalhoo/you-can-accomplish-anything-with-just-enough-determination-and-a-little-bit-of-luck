# Sorted Square Array

# O(n)
# n = len(array)

def sortedSquaredArray(array):
    positives = []
	negatives = []
	for num in array:
		if num < 0:
			negatives.append(num)
		else:
			positives.append(num)
			
	positives = [x*x for x in positives]
	negatives = list(reversed([x*x for x in negatives]))
	
	return mergeTwoSortedArrays(positives, negatives)

def mergeTwoSortedArrays(array1, array2):
	currentElementArray1 = 0
	currentElementArray2 = 0
	res = []
	while currentElementArray1 < len(array1) and currentElementArray2 < len(array2):
		if array1[currentElementArray1] <= array2[currentElementArray2]:
			res.append(array1[currentElementArray1])
			currentElementArray1 += 1
		else:
			res.append(array2[currentElementArray2])
			currentElementArray2 += 1
			
	while currentElementArray1 < len(array1):
		res.append(array1[currentElementArray1])
		currentElementArray1 += 1
		
	while currentElementArray2 < len(array2):
		res.append(array2[currentElementArray2])
		currentElementArray2 += 1
		
	return res
	