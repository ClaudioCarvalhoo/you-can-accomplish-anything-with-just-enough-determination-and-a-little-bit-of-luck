# O(n*log(n))
# n = numberOfNodes(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        self.explore(root, [], True, res)
        return res

    def explore(self, node, path, isRoot, res):
        if node is None:
            return
        if isRoot:
            path.append(str(node.val))
        else:
            path.append("->" + str(node.val))
        if node.left is None and node.right is None:
            res.append("".join(path))
        else:
            self.explore(node.left, path, False, res)
            self.explore(node.right, path, False, res)
        path.pop()