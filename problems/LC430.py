# O(n)
# n = numberOfNodes(head)

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: "Node") -> "Node":
        return self.flattenHelper(head)[0]

    def flattenHelper(self, head):
        node = head
        tail = head
        while node is not None:
            nextNode = node.next
            tail = node
            if node.child is not None:
                middleHead, middleTail = self.flattenHelper(node.child)
                node.next = middleHead
                middleHead.prev = node
                if nextNode is not None:
                    nextNode.prev = middleTail
                middleTail.next = nextNode
                node.child = None
                tail = middleTail
            node = nextNode
        return head, tail