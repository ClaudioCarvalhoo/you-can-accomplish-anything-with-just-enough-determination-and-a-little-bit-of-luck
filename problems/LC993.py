# O(n)
# n = numberOfNodes(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        level = [(root, None)]
        while len(level) > 0:
            nextLevel = []
            foundOne = False
            foundParent = None
            while len(level) > 0:
                cur, parent = level.pop()
                if cur.val == x or cur.val == y:
                    if foundOne:
                        return parent != foundParent
                    else:
                        foundOne = True
                        foundParent = parent
                if cur.left:
                    nextLevel.append((cur.left, cur))
                if cur.right:
                    nextLevel.append((cur.right, cur))
            if foundOne:
                return False
            level = nextLevel
        return False