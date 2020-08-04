class Node:
    def __init__(self, value, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous

class LinkedList:
    def __init__(self, value=None):
        if value is None:
            self.head = None
        else:
            self.head = Node(value)
        self.tail = self.head

    def print_all(self):
        current = self.head
        print('[' ,end='')
        while current != None:
            print(current.value, end=', ')
            current = current.next
        print(']')

    def insert_first(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.head.previous = Node(value, self.head, None)
            self.head = self.head.previous

    def remove_first(self):
        if self.head is None:
            raise Exception("Can't remove item from empty list")
        elif self.head.next is None:
            self.clear_list()
        else:
            self.head = self.head.next

    def insert_last(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value, None, self.tail)
            self.tail = self.tail.next

    def remove_last(self):
        if self.head is None:
            raise Exception("Can't remove item from empty list")
        elif self.head.next is None:
            self.clear_list()
        else:
            self.tail.previous.next = None
            self.tail = self.tail.previous

    def clear_list(self):
        self.head = None
        self.tail = None

    def get_head(self):
        if self.head is None:
            raise Exception("Can't retrieve head value from empty list")
        else:
            return self.head.value

    def get_tail(self):
        if self.tail is None:
            raise Exception("Can't retrieve tail value from empty list")
        else:
            return self.tail.value