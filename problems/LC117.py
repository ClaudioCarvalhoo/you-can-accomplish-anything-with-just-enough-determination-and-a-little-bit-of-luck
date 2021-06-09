# O(n) Time | O(1) Space (disregard recursion)
# n = numberOfNodes(root)
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# Sol 1
class Solution:
    def connect(self, root: "Node") -> "Node":
        self.connectChildren(root)
        return root

    def connectChildren(self, node):
        if node is None or (node.left is None and node.right is None):
            return
        nodeToPointOutside = node.left
        if node.right is not None:
            nodeToPointOutside = node.right
            if node.left is not None:
                node.left.next = node.right
        nextParent = node.next
        while nextParent is not None and (
            nextParent.left is None and nextParent.right is None
        ):
            nextParent = nextParent.next
        if nextParent is not None:
            nextOutside = nextParent.left
            if nextOutside is None:
                nextOutside = nextParent.right
            nodeToPointOutside.next = nextOutside
        self.connectChildren(node.right)
        self.connectChildren(node.left)


# Sol 2
class Solution:
    def connect(self, root: "Node") -> "Node":
        levelStart = root
        while levelStart is not None:
            node = levelStart
            nextLevelPreStart = Node()
            nextLevelTail = nextLevelPreStart
            while node is not None:
                if node.left and node.right:
                    nextLevelTail.next = node.left
                    node.left.next = node.right
                    nextLevelTail = node.right
                elif node.left:
                    nextLevelTail.next = node.left
                    nextLevelTail = node.left
                elif node.right:
                    nextLevelTail.next = node.right
                    nextLevelTail = node.right
                node = node.next
            levelStart = nextLevelPreStart.next
        return root