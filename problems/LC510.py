# O(h)
# n = height(tree)

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def inorderSuccessor(self, node: "Node") -> "Node":
        if node.right is not None:
            return self.getLeftmostNode(node.right)

        cameFrom = node
        node = node.parent
        while node is not None and cameFrom == node.right:
            cameFrom = node
            node = node.parent
        return node

    def getLeftmostNode(self, node):
        while node.left is not None:
            node = node.left
        return node