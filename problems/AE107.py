# Sort Stack

# O(n²)
# n = len(stack)

def sortStack(stack):
	if len(stack) <= 1:
		return stack
	elem = stack.pop()
    sortStack(stack)
	insertInPlace(stack, elem)
	return stack

def insertInPlace(stack, elem):
	if len(stack) == 0 or stack[-1] <= elem:
		stack.append(elem)
	else:
		temp = stack.pop()
		insertInPlace(stack, elem)
		stack.append(temp)