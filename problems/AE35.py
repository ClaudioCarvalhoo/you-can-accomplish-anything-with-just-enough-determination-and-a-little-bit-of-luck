# Min Height BST

# O(n)
# n = len(array)

def minHeightBst(array):
    if len(array) == 0:
		return None

	midpoint = len(array)//2
	root = BST(array[midpoint])
	
	populateBST(array, root, 0, midpoint-1)
	populateBST(array, root, midpoint+1, len(array)-1)
	
	return root

def populateBST(array, parent, startIndex, endIndex):
	if startIndex > endIndex:
		return
	midpoint = (startIndex + endIndex) // 2
	newValue = array[midpoint]
	newNode = BST(newValue)
	if newValue >= parent.value:
		parent.right = newNode
	else:
		parent.left = newNode
	populateBST(array, newNode, midpoint+1, endIndex)
	populateBST(array, newNode, startIndex, midpoint-1)


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
