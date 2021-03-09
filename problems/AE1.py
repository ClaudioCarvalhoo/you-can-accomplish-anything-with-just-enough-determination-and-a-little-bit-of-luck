# Two Number Sum

# O(n)
# n = len(array)

def twoNumberSum(array, targetSum):
    table = {}
	for num in array:
		needed = targetSum - num
		if needed in table:
			return [num, needed]
		table[num] = True
	return []