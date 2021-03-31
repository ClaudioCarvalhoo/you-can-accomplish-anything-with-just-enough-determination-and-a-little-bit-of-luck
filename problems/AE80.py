# Max Path Sum In Binary Tree

# O(n)
# n = numberOfNodes(tree)


class Result:
    def __init__(self, maxPath, valueAsPathPart):
        self.maxPath = maxPath
        self.valueAsPathPart = valueAsPathPart


def maxPathSum(tree):
    return explore(tree).maxPath


def explore(node):
    if node.left == None and node.right == None:
        return Result(node.value, node.value)

    maxPathFromChildren = float("-inf")
    maxPathPivotedInNode = node.value
    maxValueAsPart = node.value
    if node.left:
        leftResult = explore(node.left)
        maxPathFromChildren = max(maxPathFromChildren, leftResult.maxPath)
        maxPathPivotedInNode = max(
            maxPathPivotedInNode, maxPathPivotedInNode + leftResult.valueAsPathPart
        )
        maxValueAsPart = max(maxValueAsPart, node.value + leftResult.valueAsPathPart)
    if node.right:
        rightResult = explore(node.right)
        maxPathFromChildren = max(maxPathFromChildren, rightResult.maxPath)
        maxPathPivotedInNode = max(
            maxPathPivotedInNode, maxPathPivotedInNode + rightResult.valueAsPathPart
        )
        maxValueAsPart = max(maxValueAsPart, node.value + rightResult.valueAsPathPart)

    return Result(max(maxPathFromChildren, maxPathPivotedInNode), maxValueAsPart)
