# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def preorder(self, root, level, res):
        if root:
            if len(res) < level+1: res.append([])
            res[level].append(root.val)
            self.preorder(root.left, level+1, res)
            self.preorder(root.right, level+1, res)
            
    def levelOrderBottom(self, root):
        res=[]
        self.preorder(root, 0, res)
        res.reverse()
        return res