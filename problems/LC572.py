# O(n*m)
# n = numberOfNodes(root) | m = numberOfNodes(subRoot)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        queue = [root]
        while len(queue) > 0:
            node = queue.pop()
            if node is not None:
                equalToSubRoot = self.checkIfEqual(node, subRoot)
                if equalToSubRoot:
                    return True
                queue.append(node.left)
                queue.append(node.right)
        return False

    def checkIfEqual(self, root1, root2):
        if root1 is None or root2 is None:
            return root1 is None and root2 is None
        if root1.val != root2.val:
            return False
        return self.checkIfEqual(root1.left, root2.left) and self.checkIfEqual(
            root1.right, root2.right
        )
