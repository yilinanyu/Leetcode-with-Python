
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: 
            return False
        if not root.left and not root.right:
            return sum == root.val
        if root.left and self.hasPathSum(root.left, sum - root.val):
            return True
        if root.right and self.hasPathSum(root.right, sum - root.val):
            return True
        return False