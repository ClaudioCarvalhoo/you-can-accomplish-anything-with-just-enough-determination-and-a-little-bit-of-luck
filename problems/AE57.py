# Linked List Construction

# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(1)
    def setHead(self, node):
		self.remove(node)
		if self.head:
			self.head.prev = node
		else:
			self.tail = node
        node.prev = None
		node.next = self.head
		self.head = node

    # O(1)
    def setTail(self, node):
		self.remove(node)
		if self.tail:
			self.tail.next = node
		else:
			self.head = node
        node.prev = self.tail
		node.next = None
		self.tail = node

    # O(1)
    def insertBefore(self, node, nodeToInsert):
		self.remove(nodeToInsert)
		if node == self.head:
			self.setHead(nodeToInsert)
		else:
			nodeToInsert.next = node
			nodeToInsert.prev = node.prev
			node.prev.next = nodeToInsert
			node.prev = nodeToInsert

    # O(1)
    def insertAfter(self, node, nodeToInsert):
		self.remove(nodeToInsert)
		if node == self.tail:
			self.setTail(nodeToInsert)
		else:
			nodeToInsert.next = node.next
			nodeToInsert.prev = node
			node.next.prev = nodeToInsert
			node.next = nodeToInsert

    # O(position)
    def insertAtPosition(self, position, nodeToInsert):
		i = 1
		node = self.head
		while node:
			if i == position:
				self.remove(nodeToInsert)
				self.insertBefore(node, nodeToInsert)
				return
			i += 1
			node = node.next
		self.remove(nodeToInsert)
		self.setTail(nodeToInsert)
			
    # O(n)      
    def removeNodesWithValue(self, value):
		node = self.head
		while node:
			if node.value == value:
				self.remove(node)
			node = node.next

    # O(1)		
    def remove(self, node):
        if node == self.head:
			self.head = self.head.next
		if node == self.tail:
			self.tail = self.tail.prev
		if node.prev:
			node.prev.next = node.next
		if node.next:
			node.next.prev = node.prev

    # O(n)
    def containsNodeWithValue(self, value):
		node = self.head
		while node:
			if node.value == value:
				return True
			node = node.next
		return False