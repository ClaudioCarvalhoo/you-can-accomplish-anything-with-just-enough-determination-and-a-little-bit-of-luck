# Branch Sums

# O(n)
# n = numberOfNodes(root)

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    res = []
	explore(root, 0, res)
	return res
	
def explore(node, currentSum, res):
	currentSum += node.value
	
	if node.left == None and node.right == None:
		res.append(currentSum)
		return
	
	if node.left != None:
		explore(node.left, currentSum, res)
	if node.right != None:
		explore(node.right, currentSum, res)