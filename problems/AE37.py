# Reconstruct BST

# O(n)
# n = len(preOrderTraversalValues)

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, parent, lowerBound, upperBound, left=None, right=None):	
        self.value = value
		self.parent = parent
		self.lowerBound = lowerBound
		self.upperBound = upperBound
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
	root = BST(preOrderTraversalValues[0], None, float('-inf'), float('inf'))
	
	parent = root
    for value in preOrderTraversalValues[1:]:
		inserted = False
		while not inserted:
			if value < parent.lowerBound or value > parent.upperBound:
				parent = parent.parent
			elif value < parent.value:
				if parent.left == None:
					parent.left = BST(value, parent, parent.lowerBound, parent.value-1)
					inserted = True
				parent = parent.left
			else:
				if parent.right == None:
					parent.right = BST(value, parent, parent.value, parent.upperBound)
					inserted = True
				parent = parent.right

	return root