# O(n)
# n = number of nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if self.maxDepth(root) != False:
            return True
        else:
            return False
        
    def maxDepth(self, node):
        if node == None:
            return 1
        leftDepth = self.maxDepth(node.left)
        rightDepth = self.maxDepth(node.right)
        
        if leftDepth == False or rightDepth == False:
            return False
        
        if leftDepth > rightDepth +1 or rightDepth > leftDepth +1:
            return False
        else:
            return max(leftDepth, rightDepth) + 1