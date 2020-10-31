# O(n)
# n = numberOfNodes(root)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        return self.explore(root, {}, 0)

    def explore(self, node, soFar, over):
        if not node:
            return 0

        if node.val in soFar:
            soFar[node.val] += 1
        else:
            soFar[node.val] = 1
        if soFar[node.val] % 2 == 0:
            over -= 1
        else:
            over += 1

        if not node.left and not node.right:
            if over > 1:
                return 0
            else:
                return 1

        temp = soFar.copy()
        left = self.explore(node.left, soFar, over)
        right = self.explore(node.right, temp, over)
        return left + right