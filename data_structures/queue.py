from .linked_list import LinkedList

class Queue:
    def __init__(self):
        self.list = LinkedList()

    def enqueue(self, value):
        self.list.insert_last(value)

    def dequeue(self):
        element = self.list.get_head()
        self.list.remove_first()
        return element

    def front(self):
        return self.list.get_tail()

    def rear(self):
        return self.list.get_head()