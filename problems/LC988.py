# O(n*log(n))
# n = numberOfNodes(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        res = [chr(ord("z") + 1)]
        self.explore(root, [], res)
        return res[0]

    def explore(self, node, current, res):
        if node is None:
            return
        current.append(chr(ord("a") + node.val))
        if node.left is None and node.right is None:
            res[0] = min(res[0], "".join(reversed(current)))
        self.explore(node.left, current, res)
        self.explore(node.right, current, res)
        current.pop()
