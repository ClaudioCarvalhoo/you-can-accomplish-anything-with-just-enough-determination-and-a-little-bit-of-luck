# Array Of Products

# O(n)
# n = len(array)

def arrayOfProducts(array):
	if len(array) <= 1:
		return 0
	
    left = [array[0]]
	for i in array[1:]:
		left.append(i*left[-1])
	
	right = [array[-1]]
	for i in reversed(array[:-1]):
		right.append(i*right[-1])
	right.reverse()
		
	res = []
	for i in range(len(array)):
		leftProduct = left[i-1] if i > 0 else 1
		rightProduct = right[i+1] if i < len(array)-1 else 1
		res.append(leftProduct*rightProduct)
	return res