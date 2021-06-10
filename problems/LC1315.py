# O(n)
# n = numberOfNodes(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.helper(root, 7, 7)

    def helper(self, node, parentVal, grandparentVal):
        if node is None:
            return 0
        leftSum = self.helper(node.left, node.val, parentVal)
        rightSum = self.helper(node.right, node.val, parentVal)
        selfVal = 0
        if grandparentVal % 2 == 0:
            selfVal = node.val
        return leftSum + rightSum + selfVal