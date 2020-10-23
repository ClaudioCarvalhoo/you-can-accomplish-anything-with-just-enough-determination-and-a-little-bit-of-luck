# O(n)
# n = number of nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root == None:
            return []
        res = self.dfs(root, sum, [], 0, [])
        if res == None:
            return []
        else:
            return res

    def dfs(self, node, targetSum, path, sumSoFar, result):
        sumSoFar += node.val
        path.append(node.val)
        if node.left == None and node.right == None:
            if sumSoFar == targetSum:
                result.append(path)
                return result
            else:
                return None
        if node.left != None:
            rightResult = self.dfs(
                node.left, targetSum, path.copy(), sumSoFar, result.copy()
            )
            if rightResult != None:
                result = rightResult
        if node.right != None:
            leftResult = self.dfs(
                node.right, targetSum, path.copy(), sumSoFar, result.copy()
            )
            if leftResult != None:
                result = leftResult
        return result
