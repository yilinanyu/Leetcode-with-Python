class Solution:
    class SegmentTreeNode:
        def __init__(self, start, end, count):
            self.start, self.end, self.count = start, end, count
            self.left, self.right = None, None
        
    """
    @param A: A list of integer
    @return: The number of element in the array that 
             are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        # write your code here
        
        # build segmeng tree
        root = self.build(0, 10000)
        ans = []
        
        # modify count value for each
        for i in A:
            self.modify(root, i, 1)
        
        for i in queries:
            res = 0
            if i > 0:
                res = self.query(root, 0, i - 1)
            ans.append(res)
        
        return ans
    
    def build(self, start, end):
        if start >= end:
            return SegmentTreeNode(start, end, 0)
        
        mid = start + (end - start) / 2
        l = self.build(start, mid)
        r = self.build(mid+1, end)
        root = SegmentTreeNode(start, end, 0)
        root.left = l
        root.right = r
        return root
    
    def modify(self, root, index, value):
        if root.start == index and root.end == index:
            root.count += value
            return
    
        # query
        mid = root.start + (root.end - root.start) / 2
        if root.start <= index <= mid:
            self.modify(root.left, index, value)
        
        if mid < index <= root.end:
            self.modify(root.right, index, value)
        
        root.count = root.left.count + root.right.count
    
    def query(self, root, start, end):
        if start == root.start and end == root.end:
            return root.count
        
        mid = root.start + (root.end - root.start) / 2
        lCount = rCount = 0
        
        if start <= mid:
            if end > mid:
                lCount = self.query(root.left, start, mid)
            else:
                lCount = self.query(root.left, start, end)
        
        if end > mid:
            if start <= mid:
                rCount = self.query(root.right, mid+1, end)
            else:
                rCount = self.query(root.right, start, end)
        
        return lCount + rCount