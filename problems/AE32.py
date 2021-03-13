# BST Construction

# O(n) insertion | O(n) contains | O(n) deletion [all in worst case]
# n = numberOfNodes(self)

# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        self._insertNode(BST(value))
        return self

    def contains(self, value):
        node = self
		while node != None:
			if node.value == value:
				return True
			elif node.value > value:
				node = node.left
			else:
				node = node.right
		return False

    def remove(self, value):
        if self.left == None and self.right == None:
			return self
		
		node = self
		parent = None
		while node != None:
			if node.value == value:
				if node.right == None and node.left == None:
					if parent.value > node.value:
						parent.left = None
					else:
						parent.right = None
					break
				if node.right == None:
					node.value = node.left.value
					node.right = node.left.right
					node.left = node.left.left
					break
				elif node.right.left == None:
					node.value = node.right.value
					node.right = node.right.right
					break
				else:
					parentOfSmallestToRight = node._getParentOfSmallerToTheRight()
					node.value = parentOfSmallestToRight.left.value
					parentOfSmallestToRight.left = None
					break
			elif node.value > value:
				parent = node
				node = node.left
			else:
				parent = node
				node = node.right
        return self
	
	def _getParentOfSmallerToTheRight(self):
			parent = self.right
			while parent.left.left != None:
				parent = parent.left
			return parent

	def _insertNode(self, insertingNode):
		if insertingNode == None:
			return self
		node = self
		while node != None:
			if node.value > insertingNode.value:
				if node.left == None:
					node.left = insertingNode
					break
				node = node.left
			else:
				if node.right == None:
					node.right = insertingNode
					break
				node = node.right
        return self