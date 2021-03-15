# Binary Tree Diameter

# O(n)
# n = numberOfNodes(tree)

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    best = [float('-inf')]
	explore(tree, best)
	return best[0]
	
def explore(node, best):
	if node == None:
		return 0
	left = explore(node.left, best)
	right = explore(node.right, best)
	
	best[0] = max(best[0], left+right)
	
	return max(left, right) + 1
