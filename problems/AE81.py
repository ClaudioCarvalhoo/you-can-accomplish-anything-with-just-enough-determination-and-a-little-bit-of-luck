# Find Nodes Distance K

# O(n)
# n = numberOfNodes(tree)

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findNodesDistanceK(tree, target, k):
    res = []
	explore(tree, target, k, res)
	return res
	
def explore(node, target, k, res):
	if node == None:
		return None
	if node.value == target:
		findWithDist(node.left, k, res)
		findWithDist(node.right, k, res)
		return 1
	else:
		leftRes = explore(node.left, target, k, res)
		rightRes = explore(node.right, target, k, res)
		if leftRes == k or rightRes == k:
			res.append(node.value)
			return None
		if leftRes != None:
			findWithDist(node.right, k-leftRes, res)
			return leftRes+1
		if rightRes != None:
			findWithDist(node.left, k-rightRes, res)
			return rightRes+1
		return None
		
def findWithDist(node, k, res):
	if node != None and k != None:
		if k == 1:
			res.append(node.value)
		else:
			findWithDist(node.left, k-1, res)
			findWithDist(node.right, k-1, res)
		
		
