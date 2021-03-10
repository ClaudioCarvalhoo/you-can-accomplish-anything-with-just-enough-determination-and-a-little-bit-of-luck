# Three Number Sum

# O(n²)
# n = len(array)

def threeNumberSum(array, targetSum):
    array.sort()
	res = []
	for i in range(len(array)):
		left = i+1
		right = len(array)-1
		while left < right:
			tripletSum = array[i] + array[left] + array[right]
			if tripletSum == targetSum:
				res.append([array[i], array[left], array[right]])
				left += 1
				right -= 1
			elif tripletSum < targetSum:
				left += 1
			else:
				right -= 1
	return res
