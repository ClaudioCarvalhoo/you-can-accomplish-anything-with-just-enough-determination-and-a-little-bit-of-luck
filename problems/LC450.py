# O(h)
# h = height(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        tempRoot = TreeNode(left=root)
        self.findAndDelete(root, tempRoot, key)
        return tempRoot.left

    def findAndDelete(self, node, parent, key):
        if node is None:
            return
        elif node.val == key:
            if node.left is None and node.right is None:
                self.deleteChild(parent, node)
            elif node.right is None:
                self.overrideNodeWithSingleChild(node, node.left)
            elif node.left is None:
                self.overrideNodeWithSingleChild(node, node.right)
            else:
                self.overrideNodeWithTwoChildren(node)
        elif node.val > key:
            self.findAndDelete(node.left, node, key)
        else:
            self.findAndDelete(node.right, node, key)
        return

    def deleteChild(self, parent, child):
        if parent.left == child:
            parent.left = None
        elif parent.right == child:
            parent.right = None

    def overrideNodeWithSingleChild(self, node, child):
        node.val = child.val
        node.left, node.right = child.left, child.right

    def overrideNodeWithTwoChildren(self, node):
        tempLeft = node.left
        self.overrideNodeWithSingleChild(node, node.right)
        while node.left is not None:
            node = node.left
        node.left = tempLeft