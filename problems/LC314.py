# O(n*log(h))
# n = numberOfNodes(root) | h = height(root)

import heapq

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        columns = {}
        self.fillColumns(root, columns, 0, 0)

        res = []
        key = min(columns.keys())
        while key in columns:
            res.append([])
            while len(columns[key]) > 0:
                res[-1].append(heapq.heappop(columns[key])[2])
            key += 1
        return res

    def fillColumns(self, node, columns, curRow, curCol):
        if node is None:
            return
        if curCol not in columns:
            columns[curCol] = []
        heapq.heappush(columns[curCol], (curRow, len(columns[curCol]), node.val))
        self.fillColumns(node.left, columns, curRow + 1, curCol - 1)
        self.fillColumns(node.right, columns, curRow + 1, curCol + 1)
