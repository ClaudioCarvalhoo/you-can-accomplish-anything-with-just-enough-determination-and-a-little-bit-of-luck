# Shift Linked List

# O(n)
# n = len(linkedList)

# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    tail = head
	listLen = 1
	while tail.next != None:
		tail = tail.next
		listLen += 1
	tail.next = head
	for _ in range((listLen - k) % listLen):
		head = head.next
	tail = head
	for _ in range(listLen-1):
		tail = tail.next
	tail.next = None
	return head