# Continuous Median

import heapq

# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
class ContinuousMedianHandler:
    def __init__(self):
        self.lowerHeap = []
		self.higherHeap = []
        self.median = None

    # O(log(n))
    def insert(self, number):
		if len(self.lowerHeap) == 0 or number < self._peekLower():
			self._insertInLower(number)
			if len(self.lowerHeap) > len(self.higherHeap)+1:
				self._insertInHigher(self._popLower())
		else:
			self._insertInHigher(number)
			if len(self.higherHeap) > len(self.lowerHeap)+1:
				self._insertInLower(self._popHigher())
		
		if len(self.lowerHeap) == len(self.higherHeap):
			self.median = (self._peekLower() + self._peekHigher()) / 2
		elif len(self.lowerHeap) > len(self.higherHeap):
			self.median = self._peekLower()
		else:
			self.median = self._peekHigher()

    # O(1)
    def getMedian(self):
        return self.median

	def _insertInLower(self, number):
		heapq.heappush(self.lowerHeap, -number)
		
	def _insertInHigher(self, number):
		heapq.heappush(self.higherHeap, number)
		
	def _peekLower(self):
		return -1 * self.lowerHeap[0]
	
	def _peekHigher(self):
		return self.higherHeap[0]
	
	def _popLower(self):
		return -1 * heapq.heappop(self.lowerHeap)
	
	def _popHigher(self):
		return heapq.heappop(self.higherHeap)