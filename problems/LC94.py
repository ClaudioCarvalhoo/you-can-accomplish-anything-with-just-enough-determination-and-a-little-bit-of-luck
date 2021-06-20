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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.explore(root, res)
        return res

    def explore(self, node, res):
        if node is None:
            return
        self.explore(node.left, res)
        res.append(node.val)
        self.explore(node.right, res)


# Sol 2
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        node = root
        while node is not None or len(stack) > 0:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                res.append(node.val)
                node = node.right
        return res