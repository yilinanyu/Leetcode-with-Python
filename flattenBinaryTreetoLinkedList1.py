# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # 将左右两树分别preorder， 然后将左子树插入到根和右子树之间. 根，左，右
    def flatten(self,root):
        if root == None:
            return None
        self.flatten(root.left)
        self.flatten(root.right)
        p = root
        if p.left == None:
            return 
        p = p.left
        while p.right:
            p = p.right
        p.right = root.right
        root.right = root.left
        root.left = None
        