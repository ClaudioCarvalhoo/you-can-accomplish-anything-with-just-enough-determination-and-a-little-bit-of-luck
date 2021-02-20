# O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 

class Solution(object):
    def diameterOfBinaryTree(self, root):
        depths = {None: 0}
        self.calculateDepth(root, depths)
        
        res = 0
        q = [root]
        while len(q) > 0:
            element = q.pop(0)
            if element == None:
                continue
            else:
                q.append(element.left)
                q.append(element.right)
                res = max(res, depths[element.left]+depths[element.right])
        return res
        
       
    def calculateDepth(self, node, depths):
        if node == None:
            return 0
        elif node in depths:
            return depths[node]
        else:
            depths[node] = 1 + max(self.calculateDepth(node.left, depths), self.calculateDepth(node.right, depths))
            return depths[node]
