class Solution:
#From the pre-order array, we know that first element is the root. 
#We can find the root in in-order array. 
#Then we can identify the left and right sub-trees of the root from in-order array.

# Using the length of left sub-tree, we can identify left and right sub-trees in pre-order array. Recursively, we can build up the tree.
    def buildTree(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root