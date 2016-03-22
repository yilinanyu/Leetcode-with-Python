class SegmentTree:
    def __init__(self, A):
        self.A = A
        self.root = self.build(0, len(A) - 1)
    
    def build(self, start, end):
        if start > end:
            return None
            
        root = SegmentTreeNode(start, end, self.A[start])
        if start == end:
            return SegmentTreeNode(start, end, self.A[start])
        
        mid = start + (end - start) / 2
        
        l = self.build(start, mid)
        r = self.build(mid+1, end)
        root = SegmentTreeNode(start, end, max(l.max, r.max))
        root.left = l
        root.right = r
        return root
    
class Solution: 
    # @oaram A: a list of integer
    # @return: The root of Segment Tree
    def build(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return None
        
        tree = SegmentTree(A)
        return tree.root