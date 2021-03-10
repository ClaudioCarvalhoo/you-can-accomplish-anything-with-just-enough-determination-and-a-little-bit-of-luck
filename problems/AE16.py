# Find Three Largest Numbers

# O(n)
# n = len(array)

def findThreeLargestNumbers(array):
    res = [float('-inf'), float('-inf'), float('-inf')]
	for i in array:
		if i > res[2]:
			res.append(i)
		elif i > res[1]:
			res.insert(2, i)
		elif i > res[0]:
			res.insert(1, i)
		if len(res) > 3:
			res = res[1:]
	return res
