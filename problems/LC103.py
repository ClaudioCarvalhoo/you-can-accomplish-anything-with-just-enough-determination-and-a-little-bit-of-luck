# O(n)
# n = numberOfNodes(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        res = []
        level = 0
        curLevelQueue = [root]
        nextLevelQueue = []
        while len(curLevelQueue) > 0:
            levelRes = [node.val for node in curLevelQueue]
            if level % 2 != 0:
                levelRes.reverse()
            res.append(levelRes)
            for node in curLevelQueue:
                if node.left is not None:
                    nextLevelQueue.append(node.left)
                if node.right is not None:
                    nextLevelQueue.append(node.right)
            curLevelQueue = nextLevelQueue
            nextLevelQueue = []
            level += 1
        return res
