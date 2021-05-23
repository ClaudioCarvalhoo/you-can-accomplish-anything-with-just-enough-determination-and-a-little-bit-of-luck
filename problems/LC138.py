# O(n)
# n = len(head)

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        newListHead = Node(0)

        oldNode = head
        newNode = newListHead
        while oldNode is not None:
            newNode.next = Node(oldNode.val)
            newNode = newNode.next
            oldNode.new = newNode
            oldNode = oldNode.next

        oldNode = head
        newNode = newListHead.next
        while oldNode is not None:
            newNode.random = None if oldNode.random is None else oldNode.random.new
            oldNode = oldNode.next
            newNode = newNode.next

        return newListHead.next