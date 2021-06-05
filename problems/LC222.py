# O(log(n)²)
# n = numberOfNodes(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        height = self.calculateHeight(root)
        if self.isPerfect(root, height):
            return self.countPerfectTreeNodes(height)
        lastLevelNodes = 0
        node = root
        curHeight = 1
        while curHeight < height:
            if self.endsInSubtree(node.left, curHeight + 1, height):
                node = node.left
            else:
                node = node.right
                lastLevelNodes += 2 ** (height - curHeight - 1)
            curHeight += 1
        return self.countPerfectTreeNodes(height - 1) + lastLevelNodes

    def calculateHeight(self, root):
        height = 0
        while root is not None:
            root = root.left
            height += 1
        return height

    def countPerfectTreeNodes(self, height):
        nodes = 0
        for i in range(height):
            nodes += 2 ** i
        return nodes

    def endsInSubtree(self, node, curHeight, targetHeight):
        if curHeight == targetHeight:
            return node is None
        else:
            return self.endsInSubtree(node.right, curHeight + 1, targetHeight)

    def isPerfect(self, root, height):
        curHeight = 0
        while root is not None:
            curHeight += 1
            root = root.right
        return curHeight == height