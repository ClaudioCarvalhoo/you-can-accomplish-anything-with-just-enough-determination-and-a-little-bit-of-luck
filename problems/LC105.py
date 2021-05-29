# O(n)
# n = len(preorder)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorderPos = {}
        for i in range(len(inorder)):
            inorderPos[inorder[i]] = i
        return self.explore(preorder, 0, len(preorder) - 1, inorder, 0, inorderPos)

    def explore(
        self, preorder, preorderStart, preorderEnd, inorder, inorderStart, inorderPos
    ):
        root = preorder[preorderStart]
        node = TreeNode(root)
        leftQuant = inorderPos[root] - inorderStart
        if leftQuant > 0:
            node.left = self.explore(
                preorder,
                preorderStart + 1,
                preorderStart + leftQuant,
                inorder,
                inorderStart,
                inorderPos,
            )
        if preorderStart + 1 + leftQuant <= preorderEnd:
            node.right = self.explore(
                preorder,
                preorderStart + 1 + leftQuant,
                preorderEnd,
                inorder,
                inorderPos[root] + 1,
                inorderPos,
            )
        return node