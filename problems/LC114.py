# O(n)
# n = len(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if root is None:
            return root

        current = root
        tail = root
        stack = [root.right, root.left]
        while len(stack) > 0:
            node = stack.pop()
            if node is not None:
                tail.left = None
                tail.right = node
                stack.append(node.right)
                stack.append(node.left)
                tail = node