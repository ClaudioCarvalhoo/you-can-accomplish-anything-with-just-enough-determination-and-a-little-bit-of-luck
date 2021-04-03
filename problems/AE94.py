# Validate Three Nodes

# Sol 1
# O(h)
# h = height(tree)
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    return searchHierarchy(nodeOne, nodeTwo, nodeThree) or searchHierarchy(
        nodeThree, nodeTwo, nodeOne
    )


def searchHierarchy(ancestor, target, descendant):
    return searchNode(ancestor, target) and searchNode(target, descendant)


def searchNode(start, target):
    node = start
    while node != target:
        if node == None:
            return False
        if node.value > target.value:
            node = node.left
        else:
            node = node.right
    return True


# Sol 2
# O(d)
# d = distBetween(nodeOne, nodeThree)
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    pointerOne = nodeOne
    pointerTwo = nodeThree
    pointerOneFound = False
    pointerTwoFound = False
    while (
        pointerOne != nodeThree
        and pointerTwo != nodeOne
        and (pointerOne != None or pointerTwo != None)
    ):
        if pointerOne == nodeTwo:
            pointerOneFound = True
        if pointerTwo == nodeTwo:
            pointerTwoFound = True
        pointerOne = searchDown(pointerOne, nodeThree)
        pointerTwo = searchDown(pointerTwo, nodeOne)
    if pointerOne == nodeThree:
        return pointerOneFound
    elif pointerTwo == nodeOne:
        return pointerTwoFound
    else:
        return False


def searchDown(node, target):
    if node == None:
        return None
    if node.value > target.value:
        return node.left
    else:
        return node.right
