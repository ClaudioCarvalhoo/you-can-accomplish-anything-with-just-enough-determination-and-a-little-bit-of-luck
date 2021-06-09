# O(h)
# h = height(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        return self.searchClosest(root, target)

    def searchClosest(self, node, target):
        if node is None:
            return float("inf")
        if node.val == target:
            return node.val

        subTreeRes = float("inf")
        if node.val > target:
            subTreeRes = self.searchClosest(node.left, target)
        elif node.val < target:
            subTreeRes = self.searchClosest(node.right, target)
        return self.getClosestOfTwoValues(node.val, subTreeRes, target)

    def getClosestOfTwoValues(self, val1, val2, target):
        if abs(val1 - target) <= abs(val2 - target):
            return val1
        return val2