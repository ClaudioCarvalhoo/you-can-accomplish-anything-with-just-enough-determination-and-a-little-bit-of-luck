# O(n)
# n = numberOfNodes(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Sol 1 | O(n) Space
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        depths = {}
        self.findMaxDepth(root, depths)

        node = root
        while depths[node] != 0:
            if node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            elif depths[node.left] >= depths[node.right]:
                node = node.left
            else:
                node = node.right
        return node.val

    def findMaxDepth(self, node, depths):
        if node is None:
            return -1
        depths[node] = (
            max(
                self.findMaxDepth(node.left, depths),
                self.findMaxDepth(node.right, depths),
            )
            + 1
        )
        return depths[node]


# Sol 2 | O(log(n)) Space
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        res = [root.val, 0]
        self.explore(root, 0, res)
        return res[0]

    def explore(self, node, depth, res):
        if node is None:
            return
        if depth > res[1]:
            res[0] = node.val
            res[1] = depth
        self.explore(node.left, depth + 1, res)
        self.explore(node.right, depth + 1, res)


# Sol 3 | O(n) Space
from collections import deque


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        resNode = root
        resDepth = 0
        queue = deque([(root, 0)])
        while len(queue) > 0:
            node, depth = queue.popleft()
            if depth > resDepth:
                resNode, resDepth = node, depth
            if node.left is not None:
                queue.append((node.left, depth + 1))
            if node.right is not None:
                queue.append((node.right, depth + 1))
        return resNode.val