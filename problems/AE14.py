# Product Sum

# O(n)
# n = lenIncludingSubelements(array)

# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, depth=1):
	res = 0
    for i in array:
		if type(i) is int:
			res += i
		else:
			res += productSum(i, depth+1)
	return res * depth
