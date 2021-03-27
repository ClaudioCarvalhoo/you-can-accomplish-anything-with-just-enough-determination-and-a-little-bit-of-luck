# Powerset

# O(2ⁿ*n)
# n = len(array)

def powerset(array):
    res = [[]]
	for i in array:
		for prevIdx in range(len(res)):
			res.append(res[prevIdx] + [i])
	return res
