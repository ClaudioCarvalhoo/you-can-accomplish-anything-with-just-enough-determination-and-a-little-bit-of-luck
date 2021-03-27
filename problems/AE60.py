# Permutations

# Sol 1
# O(n!*n²)
def getPermutations(array):
    nums = set(array)
	if len(nums) <= 0:
		return []
	return buildPermutations([], nums)
	
def buildPermutations(prefix, nums):
	if len(nums) <= 0:
		return [prefix]
	res = []
	for i in nums:
		res += buildPermutations(prefix + [i], nums-set([i]))
	return res


# Sol 2
# O(n!*n)
def getPermutations(array):
	if len(array) <= 0:
		return []
	return buildPermutations([], array, 0)
	
def buildPermutations(prefix, array, start):
	if start >= len(array):
		return [prefix]
	res = []
	for i in range(start, len(array)):
		swap(array, start, i)
		res += buildPermutations(prefix + [array[start]], array, start+1)
		swap(array, i, start)
	return res

def swap(array, i, j):
	array[i], array[j] = array[j], array[i]