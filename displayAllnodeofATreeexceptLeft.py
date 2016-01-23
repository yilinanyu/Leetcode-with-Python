class Solution:
   
    def displaynodeexceptLeftMost(root1):
        if id(root1)!= root:
            print root1
        else:
            



    def disPlayLeftNode(root):

        if root is None:
            return None
        elif root.left is None:
            return root
        else:
            self.disPlayLeftNode(root.left)