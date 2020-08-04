from .linked_list import LinkedList

class Stack:
    def __init__(self):
        self.list = LinkedList()

    def insert(self, value):
        self.list.insert_first(value)

    def pop(self):
        element = self.list.get_head()
        self.list.remove_first()
        return element

    def peek(self):
        return self.list.get_head()