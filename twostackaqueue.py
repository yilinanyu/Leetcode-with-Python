class Queue(object):
    #two stack: inStack and OutStack"
    #inStack  接受push操作新增的元素，outStack 为pop/peak 提供服务
    #若outstack 为空，将instack 所有元素弹出并压入outstack，然后对outstack 进行相应操作。

# 由于栈具有后进先出（Last In First Out）的性质，栈A中的元素依次弹出并压入空栈B之后，栈A中元素的顺序会被逆转

# 当执行pop或者peek操作时，如果outStack中元素为空，则将inStack中的所有元素弹出并压入outStack，然后对outStack执行相应操作

# 由于元素至多只会从inStack向outStack移动一次，因此peek/pop操作的平摊开销为O(1)
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
        # 看是否空
        self.peek()
        # 非空才pop
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