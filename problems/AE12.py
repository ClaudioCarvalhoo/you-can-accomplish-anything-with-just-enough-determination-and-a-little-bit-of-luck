# Remove Duplicates From Linked List

# O(n)
# n = len(linkedList)

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    node = linkedList
	while node != None:
		while node.next != None and node.next.value == node.value:
			node.next = node.next.next
		node = node.next
	return linkedList
