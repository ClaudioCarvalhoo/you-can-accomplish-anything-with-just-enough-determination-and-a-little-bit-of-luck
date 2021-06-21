# O(n)
# n = numberOfNodes(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return self.explore(root)[0]

    def explore(self, node):
        if node is None:
            return (float("-inf"), float("-inf"))

        leftRes, maxLineLeft = self.explore(node.left)
        rightRes, maxLineRight = self.explore(node.right)

        bestSumAsJoint = node.val + max(0, maxLineLeft) + max(0, maxLineRight)
        bestLineWithNode = node.val + max(0, maxLineLeft, maxLineRight)

        return (max(leftRes, rightRes, bestSumAsJoint), bestLineWithNode)