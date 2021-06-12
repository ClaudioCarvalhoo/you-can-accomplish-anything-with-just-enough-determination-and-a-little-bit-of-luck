# O(n*log(n))
# n = numberOfNodes(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        buckets = {}
        self.explore(root, buckets, 0, 0)
        minKey = float("inf")
        maxKey = float("-inf")
        for key in buckets:
            buckets[key].sort(key=lambda x: (x[1], x[0]))
            minKey = min(minKey, key)
            maxKey = max(maxKey, key)
        res = []
        for key in range(minKey, maxKey + 1):
            res.append([x[0] for x in buckets[key]])
        return res

    def explore(self, node, buckets, row, col):
        if node is None:
            return
        if col not in buckets:
            buckets[col] = []
        buckets[col].append((node.val, row))
        self.explore(node.left, buckets, row + 1, col - 1)
        self.explore(node.right, buckets, row + 1, col + 1)
