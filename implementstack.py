#push(x) -- 使用queue的push to back操作.
#pop() -- 将queue中除队尾外的所有元素pop from front然后push to back，最后执行一次pop from front
#top() -- 将queue中所有元素pop from front然后push to back，使用辅助变量top记录每次弹出的元素，返回top
#empty() -- 使用queue的is empty操作.
class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.queue = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.queue.append(x)

    # @return nothing
    def pop(self):
        for x in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))
        self.queue.pop(0)

    # @return an integer
    def top(self):
        top = None
        for x in range(len(self.queue)):
            top = self.queue.pop(0)
            self.queue.append(top)
        return top

    # @return an boolean
    def empty(self):
        return self.queue == []