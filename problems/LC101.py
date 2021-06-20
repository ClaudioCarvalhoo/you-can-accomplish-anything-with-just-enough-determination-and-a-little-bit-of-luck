# O(n)
# n = numberOfNodes(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Sol 1
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.areSubtreesSymmetric(root.left, root.right)

    def areSubtreesSymmetric(self, node1, node2):
        if node1 is None or node2 is None:
            return node1 is None and node2 is None

        if node1.val != node2.val:
            return False

        return self.areSubtreesSymmetric(
            node1.left, node2.right
        ) and self.areSubtreesSymmetric(node1.right, node2.left)


# Sol 2
from collections import deque


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = deque([(root.left, root.right)])
        while len(queue) > 0:
            node1, node2 = queue.popleft()
            if node1 is None or node2 is None:
                if node1 is not None or node2 is not None:
                    return False
            else:
                if node1.val != node2.val:
                    return False
                queue.append((node1.left, node2.right))
                queue.append((node1.right, node2.left))
        return True
