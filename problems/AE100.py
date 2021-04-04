# Find Loop

# O(n)
# n = len(linkedList)

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    nodeInLoop = findNodeInLoop(head)
    loopSize = calculateLoopSize(nodeInLoop)
    return findFirstOfLoop(head, loopSize)


def findNodeInLoop(node):
    lookAhead = node.next
    while node != lookAhead:
        node = node.next
        lookAhead = lookAhead.next.next
    return node


def calculateLoopSize(nodeInLoop):
    loopSize = 1
    lookAhead = nodeInLoop.next
    while lookAhead != nodeInLoop:
        lookAhead = lookAhead.next
        loopSize += 1
    return loopSize


def findFirstOfLoop(node, loopSize):
    lookAhead = node
    for _ in range(loopSize):
        lookAhead = lookAhead.next
    while node != lookAhead:
        node = node.next
        lookAhead = lookAhead.next
    return node
