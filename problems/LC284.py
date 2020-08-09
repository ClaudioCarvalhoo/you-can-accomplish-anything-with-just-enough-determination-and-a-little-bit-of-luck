# init: O(1) | peek: O(1) | next: O(1) | hasNext: O(1)
# Assuming that the iterator methods are O(1) and discounting for the possible internal list resizing when appending to the queue.

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

from collections import deque 

class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.cache = deque()
        
    def peek(self):
        if len(self.cache) > 0:
            return self.cache[0]
        else:
            next = self.iterator.next()
            self.cache.append(next)
            return next
        
    def next(self):
        if len(self.cache) > 0:
            return self.cache.popleft()
        else:
            return self.iterator.next()

    def hasNext(self):
        return self.iterator.hasNext() or len(self.cache) > 0
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].