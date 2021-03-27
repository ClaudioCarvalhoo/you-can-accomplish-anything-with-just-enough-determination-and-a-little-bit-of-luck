# Min Heap Construction


import math

# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

	# O(n(log(n)))
    def buildHeap(self, array):
        return sorted(array)

	# O(log(n))
    def siftDown(self, valIndex):
		leftChildIndex = self._getRightChildIndex(valIndex)
		rightChildIndex = self._getLeftChildIndex(valIndex)
		while leftChildIndex or rightChildIndex:
			value = self.heap[valIndex]
			smallestChildIndex = leftChildIndex
			if not leftChildIndex or self.heap[rightChildIndex] < self.heap[leftChildIndex]:
				smallestChildIndex = rightChildIndex
			if value > self.heap[smallestChildIndex]:
				self._swap(valIndex, smallestChildIndex)
				valIndex = smallestChildIndex
				leftChildIndex = self._getRightChildIndex(valIndex)
				rightChildIndex = self._getLeftChildIndex(valIndex)
			else:
				break

	# O(log(n))
    def siftUp(self, valIndex):
		value = self.heap[valIndex]
		parentIndex = self._getParentIndex(valIndex)
		while parentIndex and self.heap[parentIndex] > value:
			self._swap(valIndex, parentIndex)
			valIndex = parentIndex
			parentIndex = self._getParentIndex(valIndex)

	# O(1)
    def peek(self):
        return self.heap[0]

	# O(log(n))
    def remove(self):
        removedValue = self.peek()
		self.heap[0] = self.heap[-1]
		del self.heap[-1]
		self.siftDown(0)
		return removedValue

	# O(log(n))
    def insert(self, value):
        self.heap.append(value)
		self.siftUp(len(self.heap)-1)
	
	def _getLeftChildIndex(self, i):
		childIndex = (i*2)+1
		if childIndex < len(self.heap):
			return childIndex
		else:
			return None
		
	def _getRightChildIndex(self, i):
		childIndex = (i*2)+2
		if childIndex < len(self.heap):
			return childIndex
		else:
			return None
		
	def _getParentIndex(self, i):
		if i > 0:
			return math.floor((i-1)/2)
		else:
			return None
		
	def _swap(self, i, j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
