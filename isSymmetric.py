# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.helper(root.left,root.right)
    def helper(self, l, r):
        if l is None and r is None:
            return True
        elif l and r and l.val== r.val:
            return self.helper(l.left,r.right) and self.helper(l.right, r.left)
        return False
        
        
        
        