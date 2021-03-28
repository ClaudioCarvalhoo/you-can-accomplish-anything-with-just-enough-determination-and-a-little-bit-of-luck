# Min Max Stack Construction

# O(1) all operations

# Feel free to add new properties and methods to the class.
class MinMaxStack:
	def __init__(self):
		self.stack = []
		self.minStack = []
		self.maxStack = []
		
    def peek(self):
		if len(self.stack) <= 0:
			return None
        return self.stack[-1]

    def pop(self):
        popped = self.stack[-1]
		del self.stack[-1]
		if popped == self.getMin():
			del self.minStack[-1]
		if popped == self.getMax():
			del self.maxStack[-1]
		return popped

    def push(self, number):
        self.stack.append(number)
		if self.getMin() == None or number <= self.getMin():
			self.minStack.append(number)
		if self.getMax() == None or number >= self.getMax():
			self.maxStack.append(number)

    def getMin(self):
		if len(self.minStack) <= 0:
			return None
        return self.minStack[-1]

    def getMax(self):
		if len(self.maxStack) <= 0:
			return None
        return self.maxStack[-1]
