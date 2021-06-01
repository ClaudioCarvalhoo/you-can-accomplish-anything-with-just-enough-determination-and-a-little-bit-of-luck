# O(n)
# n = numberOfNodes(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        levels = {}
        self.explore(root, levels, 1, 0)
        width = 0
        for level in levels:
            width = max(width, levels[level]["right"] - levels[level]["left"] + 1)
        return width

    def explore(self, node, levels, curLevel, curPosition):
        if node is None:
            return
        if curLevel not in levels:
            levels[curLevel] = {"left": float("inf"), "right": float("-inf")}
        levels[curLevel]["left"] = min(levels[curLevel]["left"], curPosition)
        levels[curLevel]["right"] = max(levels[curLevel]["right"], curPosition)
        self.explore(node.left, levels, curLevel + 1, 2 * curPosition)
        self.explore(node.right, levels, curLevel + 1, (2 * curPosition) + 1)
