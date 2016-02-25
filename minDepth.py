# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
    #     """
    # 错误解法： 因为对于1，2 来说应该返回2， 我的解法，返回1
    #     if root is None:
    #         return 0
    #     return min(self.height(root.left), self.height(root.right)) + 1
    # def height(self, root):
    #     if root is None:
    #         return 0
    #     return max (self.height(root.left), self.height(root.right)) + 1
    # 正确解法：需要对左为0 和右为0单独考虑
        if root is None:
            return 0
        elif root.left is None:
            return self.minDepth(root.right) + 1
        elif root.right is None:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        