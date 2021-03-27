# Remove Kth Node From End

# O(n)
# n = len(head)

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    node = head
    lookAhead = node
    for _ in range(k):
        lookAhead = lookAhead.next
    if lookAhead == None:
        node.value = node.next.value
        node.next = node.next.next
    else:
        while lookAhead.next != None:
            node = node.next
            lookAhead = lookAhead.next
        node.next = node.next.next
