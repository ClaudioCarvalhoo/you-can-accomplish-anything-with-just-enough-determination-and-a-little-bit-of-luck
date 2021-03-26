# Youngest Common Ancestor

# O(n)
# n = height(topAncestor)

# Sol 1
# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
	depthOne = calculateDepth(descendantOne)
	depthTwo = calculateDepth(descendantTwo)

	while descendantOne != descendantTwo:
		if depthOne == depthTwo:
			descendantOne = descendantOne.ancestor
			descendantTwo = descendantTwo.ancestor
		elif depthOne > depthTwo:
			descendantOne = descendantOne.ancestor
			depthOne -= 1
		else:
			descendantTwo = descendantTwo.ancestor
			depthTwo -= 1
			
	return descendantOne
    
def calculateDepth(node):
	depth = 0
	while node.ancestor != None:
		node = node.ancestor
		depth += 1
	return depth


# Sol 2 -- This assumes that names are unique and hasheable
# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
	ancestorsOfOne = set()
    while descendantOne != None:
		ancestorsOfOne.add(descendantOne.name)
		descendantOne = descendantOne.ancestor
	while descendantTwo != None:
		if descendantTwo.name in ancestorsOfOne:
			return descendantTwo
		descendantTwo = descendantTwo.ancestor
	return topAncestor
