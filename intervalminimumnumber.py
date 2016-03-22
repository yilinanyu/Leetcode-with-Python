"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
maxInt = 2147483647
class Node(object):
    def __init__(self, start, end, m):
        self.start, self.end, self.m = start, end, m
        self.left, self.right = None, None
    
class SegmentTree(object):
    def __init__(self, A):
        self.A = A
        self.root = self.build(0, len(A) - 1)
    
    def build(self, start, end):
        if start > end:
            return None
        elif start == end:
            return Node(start, end, self.A[start])
        
        mid = start + (end - start) / 2
        l = self.build(start, mid)
        r = self.build(mid+1, end)
        
        if l:
            lMin = min(maxInt, l.m)
        
        if r:
            rMin = min(maxInt, r.m)
        
        root = Node(start, end, min(lMin, rMin))
        root.left = l
        root.right = r
        return root
    
    def query(self, root, start, end):
        if root is None or start > end:
            return maxInt
        
        if start == root.start and end == root.end:
            return root.m
        
        mid = root.start + (root.end - root.start) / 2
        lMin = rMin = maxInt
        
        if start <= mid:
            if end > mid:
                lMin = self.query(root.left, start, mid)
            else:
                lMin = self.query(root.left, start, end)
        
        if end > mid:
            if start <= mid:
                rMin = self.query(root.right, mid+1, end)
            else:
                rMin = self.query(root.right, start, end)
        
        return min(lMin, rMin)
        
        
        
class Solution: 
    """
    @param A, queries: Given an integer array and an Interval list
                       The ith query is [queries[i-1].start, queries[i-1].end]
    @return: The result list
    """
    def intervalMinNumber(self, A, queries):
        # write your code here
        ans = []
        tree = SegmentTree(A)
        for q in queries:
            ans.append(tree.query(tree.root, q.start, q.end))
        return ans