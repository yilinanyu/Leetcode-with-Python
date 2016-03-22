class Solution:
    """
    @param A: A list of integer
    @return: Count the number of element before this element 'ai' is 
             smaller than it and return count number list
    """
    def countOfSmallerNumberII(self, A):
        # write your code here
        root = self.build(0, 10000)
        
        ans = []    
        for i in A:
            res = 0
            if i > 0:
                res = self.query(root, 0, i - 1)
            self.modify(root, i)
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
    
    def modify(self, root, index):
        if root.start == index and root.end == index:
            root.count += 1
            return
    
        # query
        mid = root.start + (root.end - root.start) / 2
        if root.start <= index <= mid:
            self.modify(root.left, index)
        
        if mid < index <= root.end:
            self.modify(root.right, index)
        
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