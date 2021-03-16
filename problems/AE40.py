# Find Successor

# O(n) worst case, when tree is completely unbalanced
# n = numberOfNodes(tree)

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    if node.right:
		node = node.right
		while node.left != None:
			node = node.left
		return node
	elif node.parent == None:
		return None
	elif node.parent.left == node:
		return node.parent
	else:
		return node.parent.parent
	
