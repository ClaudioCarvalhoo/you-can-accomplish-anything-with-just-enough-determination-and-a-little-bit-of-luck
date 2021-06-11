# O(n)
# n = len(pre)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        postPos = {}
        for i in range(len(post)):
            postPos[post[i]] = i

        root = TreeNode(pre[0])
        stack = [root]
        for i in range(1, len(pre)):
            num = pre[i]
            while postPos[num] > postPos[stack[-1].val] or (
                stack[-1].left is not None and stack[-1].right is not None
            ):
                stack.pop()
            node = stack[-1]
            if node.left is None:
                node.left = TreeNode(num)
                stack.append(node.left)
            else:
                node.right = TreeNode(num)
                stack.append(node.right)
        return root
