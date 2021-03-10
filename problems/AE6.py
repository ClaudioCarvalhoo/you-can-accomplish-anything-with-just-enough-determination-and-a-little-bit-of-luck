# Find Closest Value In BST

# O(n*log(n))
# n = numberOfElements(tree)

def findClosestValueInBst(tree, target):
    node = tree
	currentBest = node.value
	while node != None:
		if abs(target-node.value) < abs(target-currentBest):
			currentBest = node.value
		if node.value > target:
			node = node.left
		else:
			node = node.right
	return currentBest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
