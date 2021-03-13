# Find Kth Largest Value In BST

# O()
# 

# Sol 1
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, target):
    return explore(tree, 0, target).value
	
def explore(node, current, target):
	if node.right:
		rightRes = explore(node.right, current, target)
		if rightRes.found:
			return rightRes
		else:
			current = rightRes.nodesSeen
	
	current += 1
	if current == target:
		return ExploreRes(current, True, node.value)
		
	if node.left:
		leftRes = explore(node.left, current, target)
		if leftRes.found:
			return leftRes
		else:
			current = leftRes.nodesSeen
			
	return ExploreRes(current, False, None)

class ExploreRes:
	def __init__(self, nodesSeen, found, value):
		self.nodesSeen = nodesSeen
		self.found = found
		self.value = value

# Sol 2
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, target):
	res = ExploreRes(0 , None)
    explore(tree, res, target)
	return res.value
	
def explore(node, res, target):
	if node == None or res.nodesSeen >= target:
		return
	
	explore(node.right, res, target)
	
	if res.nodesSeen < target:
		res.nodesSeen += 1
		res.value = node.value
	
	explore(node.left, res, target)

class ExploreRes:
	def __init__(self, nodesSeen, value):
		self.nodesSeen = nodesSeen
		self.value = value