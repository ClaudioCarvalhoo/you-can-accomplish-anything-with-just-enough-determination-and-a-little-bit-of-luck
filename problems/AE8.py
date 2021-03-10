# Node Depths

# O(n)
# n = numberOfNodes(root)


def nodeDepths(root):
    return explore(root, 0)


def explore(node, depth):
    if node == None:
        return 0

    leftDepthSum = explore(node.left, depth + 1)
    rightDepthSum = explore(node.right, depth + 1)
    return depth + leftDepthSum + rightDepthSum


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
