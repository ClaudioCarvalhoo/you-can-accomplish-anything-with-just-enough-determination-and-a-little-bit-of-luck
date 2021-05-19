# Next Greater Element

# O(n)
# n = len(array)

def nextGreaterElement(array):
    res = [None for _ in range(len(array))]
	inRes = 0
	
	stack = []
	i = 0
	while inRes < len(array):
		curIndex = i%len(array)
		while len(stack) > 0 and stack[-1][1] <= i - len(array):
			elem = stack.pop()
			res[elem[1]] = -1
			inRes += 1
		while len(stack) > 0 and array[curIndex] > stack[-1][0]:
			elem = stack.pop()
			res[elem[1]] = array[curIndex]
			inRes += 1
		if res[i%len(array)] is None:
			stack.append((array[curIndex], curIndex))
		i += 1
		
	return res
