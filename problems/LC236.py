# O(n)
# n = tree nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pathToP = self.pathToNode(root, p.val, [])
        pathToQ = self.pathToNode(root, q.val, [])
        
        start = min(len(pathToP), len(pathToQ)) -1
        
        for i in range(start, -1, -1):
            if pathToP[i].val == pathToQ[i].val:
                return pathToP[i]
        
    def pathToNode(self, currentNode, targetVal, pathSoFar):
        pathSoFar.append(currentNode)
        if currentNode.val == targetVal:
            return pathSoFar
        if currentNode.left != None:
            left = self.pathToNode(currentNode.left, targetVal, pathSoFar.copy())
            if left != []:
                return left
        if currentNode.right != None:
            right = self.pathToNode(currentNode.right, targetVal, pathSoFar.copy())
            if right != []:
                return right
        return []
        