# O(n)
# n = numberOfNodes(root)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        res = []
        self.explore(root, res)
        return sum(res)

    def explore(self, node, res):
        if node == None:
            return 0
        leftSum = self.explore(node.left, res)
        rightSum = self.explore(node.right, res)

        tilt = abs(leftSum - rightSum)

        res.append(tilt)

        return leftSum + rightSum + node.val
