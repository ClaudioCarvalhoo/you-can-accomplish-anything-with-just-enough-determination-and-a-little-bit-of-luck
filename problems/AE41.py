# Height Balanced Binary Tree

# O(n)
# n = numberOfNodes(tree)

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
    return explore(tree, 0)[1]


def explore(node, depth):
    if node == None:
        return (depth, True)

    leftSubtree = explore(node.left, depth + 1)
    rightSubtree = explore(node.right, depth + 1)

    unbalanced = abs(leftSubtree[0] - rightSubtree[0]) > 1
    childrenUnbalanced = not (leftSubtree[1] and rightSubtree[1])
    if unbalanced or childrenUnbalanced:
        return (-1, False)
    else:
        return (max(leftSubtree[0], rightSubtree[0]), True)
