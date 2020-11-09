# O(n)
# n = numberOfNodes(root)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        return self.explore(root, root.val, root.val)

    def explore(self, node, maxSoFar, minSoFar):
        if node == None:
            return float("-inf")

        compareToMax = abs(maxSoFar - node.val)
        compareToMin = abs(minSoFar - node.val)

        bestWithThisNode = max(compareToMax, compareToMin)

        maxSoFar = max(maxSoFar, node.val)
        minSoFar = min(minSoFar, node.val)

        leftResult = self.explore(node.left, maxSoFar, minSoFar)
        rightResult = self.explore(node.right, maxSoFar, minSoFar)

        return max(bestWithThisNode, leftResult, rightResult)