class Queue(object):
	# use two stack:inStack and outStack 
	# instack deal with the push, outstack deal with the pop and peak 
	# when outstack is empty and pop the instack and push to the outStack
	def _init_(self):
		self.inStack = []
		self.outstack = []
	def push(self,x):
		self.inStack.append(x)
	def pop(self,x):
		self.peak()
		self.outstack.pop()
	def peak(self):
		if not self.outstack:
			# when outstack is vacant
			while self.instack:
				self.outStack.append(self.instack.pop())
