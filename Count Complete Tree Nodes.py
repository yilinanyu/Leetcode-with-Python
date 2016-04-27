# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#   1
#  2  3
# 1 3 3
# two case: full 2^n - 1 + 2^n  or not full 2^n - 1 + l(find the first not empty)
# depth of current index == depth of tree: full 
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        depth = 0
        temp = root
        while temp:
            temp = temp.left
            depth += 1
        n = 2**(depth - 1)
        l = 0
        r = n - 1 
     
        # full tree 
        if self.getdepth(root, r, n/2) == depth:
            return 2*n - 1
        # not full 

        while l < r:
            mid = l + (r - l)/2
            if self.getdepth(root, mid, n/2) != depth:
                r = mid
            else:
                l = mid + 1
        return l + n - 1
    # 用非递归的方法根据index求depth
    def getdepth(self, root, k, half):
        depth = 0
        while root:
            if k >= half:
                root = root.right
                k -= half
            else:
                root = root.left
            
            half /= 2
            depth += 1
        return depth
        
            
            
        
        