# O(n)
# n = numberOfNodes(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        res = [0]
        self.explore(root, res)
        return res[0]

    def explore(self, node, res):
        if node is None:
            return [True, 0, float("-inf"), float("inf")]
        isLeftBst, leftQuant, leftMax, leftMin = self.explore(node.left, res)
        isRightBst, rightQuant, rightMax, rightMin = self.explore(node.right, res)

        subTreeQuant = leftQuant + rightQuant + 1
        isSubTreeBst = (
            isLeftBst and isRightBst and leftMax < node.val and rightMin > node.val
        )

        if isSubTreeBst and subTreeQuant > res[0]:
            res[0] = subTreeQuant

        return [
            isSubTreeBst,
            subTreeQuant,
            max(node.val, leftMax, rightMax),
            min(node.val, leftMin, rightMin),
        ]
