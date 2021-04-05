# Reverse Linked List

# O(n)
# n = len(linkedList)

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
	node = head
    nextNode = head.next
	head.next = None
	while nextNode != None:
		temp = nextNode.next
		nextNode.next = node
		node = nextNode
		nextNode = temp
	return node
