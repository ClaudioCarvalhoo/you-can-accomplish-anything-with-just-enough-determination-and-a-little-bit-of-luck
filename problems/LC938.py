# O(n)
# n = numberOfNodes(root)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        total = 0
        return self.explore(root, low, high)
        
    def explore(self, node, low, high):
        if node == None:
            return 0
        cur = node.val
        if cur < low or cur > high:
            cur = 0
        return cur + self.explore(node.left, low, high) + self.explore(node.right, low, high)
        