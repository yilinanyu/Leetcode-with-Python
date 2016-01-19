class Queue(object):
    #two stack: inStack and OutStack"
    #inStack  接受push操作新增的元素，outStack 为pop/peak 提供服务
    #若outstack 为空，将instack 所有元素弹出并压入outstack，然后对outstack 进行相应操作。
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.inStack = []
        self.outStack = []
    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.inStack.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        self.peek()
        self.outStack.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]
        
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.inStack) + len(self.outStack) == 0