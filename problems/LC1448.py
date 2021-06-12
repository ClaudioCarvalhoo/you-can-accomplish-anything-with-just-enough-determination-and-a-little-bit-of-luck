# O(n)
# n = numberOfNodes(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.countGood(root, float("-inf"))

    def countGood(self, node, maxSeen):
        if node is None:
            return 0
        goodNode = 1 if maxSeen <= node.val else 0
        maxSeen = max(maxSeen, node.val)
        return (
            goodNode
            + self.countGood(node.left, maxSeen)
            + self.countGood(node.right, maxSeen)
        )
