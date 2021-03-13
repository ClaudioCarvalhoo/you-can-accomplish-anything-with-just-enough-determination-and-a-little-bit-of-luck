# Validate BST

# O(n)
# n = numberOfNodes(tree)

# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return explore(tree)


def explore(node, lowerBound=float("-inf"), upperBound=float("inf")):
    if node == None:
        return True

    leftValid = True
    if node.left != None:
        leftValid = node.left.value < node.value and node.left.value >= lowerBound
        leftValid = leftValid and explore(node.left, lowerBound, node.value)

    rightValid = True
    if node.right != None:
        rightValid = node.right.value >= node.value and node.right.value < upperBound
        rightValid = rightValid and explore(node.right, node.value, upperBound)

    return leftValid and rightValid
