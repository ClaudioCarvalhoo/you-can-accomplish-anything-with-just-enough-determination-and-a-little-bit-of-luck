# Breadth-first Search

# O(n)
# n = numberOfNodesBelow(self)

# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
		array.append(self)
		i = 0
		while i < len(array):
			array += array[i].children
			i += 1
		array = [node.name for node in array]
		return array
