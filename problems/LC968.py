# O(n)
# numberOfNodes(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        return self.setupCameras(root, True)[2]

    def setupCameras(self, node, isRoot):
        if node is None:
            return (False, True, 0)
        if not isRoot and node.left is None and node.right is None:
            return (False, False, 0)

        coveredByLeft, isLeftCovered, leftCameras = self.setupCameras(node.left, False)
        coveredByRight, isRightCovered, rightCameras = self.setupCameras(
            node.right, False
        )

        if (
            (not isLeftCovered)
            or (not isRightCovered)
            or (isRoot and (not coveredByLeft) and (not coveredByRight))
        ):
            return (True, True, leftCameras + rightCameras + 1)
        else:
            return (False, coveredByLeft or coveredByRight, leftCameras + rightCameras)