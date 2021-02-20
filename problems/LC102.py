# O(n)
# n = numberOfNodes(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [(root, 0)]
        res = []
        while len(queue) > 0:
            current = queue.pop(0)
            currentNode = current[0]
            currentLevel = current[1]
            if currentNode == None:
                continue
            if len(res) <= currentLevel:
                res.append([currentNode.val])
            else:
                res[currentLevel].append(currentNode.val)
            queue.append((currentNode.left, currentLevel + 1))
            queue.append((currentNode.right, currentLevel + 1))
        return res