# O(n)
# n = numberOfNodes(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(
        self, root: TreeNode, leftBound=float("-inf"), rightBound=float("inf")
    ) -> bool:
        if root is None:
            return True
        return (
            leftBound < root.val < rightBound
            and self.isValidBST(root.left, leftBound, root.val)
            and self.isValidBST(root.right, root.val, rightBound)
        )
