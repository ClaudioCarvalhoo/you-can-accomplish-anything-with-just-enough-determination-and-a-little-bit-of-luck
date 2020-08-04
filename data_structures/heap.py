import math

class MinHeap:

    def __init__(self):
        self.items = []

    def _get_left_child_index(self, parent_index):
        return (2*parent_index)+1
    
    def _get_right_child_index(self, parent_index):
        return (2*parent_index)+2

    def _get_parent_index(self, index):
        return math.floor((index-1)/2)

    def _has_left_child(self, parent_index):
        return self._get_left_child_index(parent_index) < len(self.items)

    def _has_right_child(self, parent_index):
        return self._get_right_child_index(parent_index) < len(self.items)

    def _has_parent(self, index):
        return self._get_parent_index(index) >= 0

    def _heapify_down(self):
        index = 0
        while self._has_left_child(index):
            smallest_child_index = self._get_left_child_index(index)
            if self._has_right_child(index) and self.items[self._get_right_child_index(index)] < self.items[self._get_left_child_index(index)]:
                smallest_child_index = self._get_right_child_index(index)
            if self.items[index] > self.items[smallest_child_index]:
                self._swap(index, smallest_child_index)
                index = smallest_child_index
            else:
                break

    def _heapify_up(self):
        index = len(self.items)-1
        while self._has_parent(index) and self.items[index] < self.items[self._get_parent_index(index)]:
            self._swap(index, self._get_parent_index(index))
            index = self._get_parent_index(index)

    def _swap(self, index1, index2):
        temp = self.items[index1]
        self.items[index1] = self.items[index2]
        self.items[index2] = temp

    def peek(self):
        if len(self.items) <= 0:
            raise Exception("Can't retrieve item from empty heap")
        else:
            return self.items[0]

    def pop(self):
        if len(self.items) <= 0:
            raise Exception("Can't retrieve item from empty heap")
        elif len(self.items) == 1:
            return self.items.pop()
        else:
            value = self.items[0]
            self.items[0] = self.items.pop()
            self._heapify_down()
            return value
    
    def insert(self, value):
        self.items.append(value)
        self._heapify_up()