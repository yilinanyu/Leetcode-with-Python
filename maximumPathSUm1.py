# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
#     DFS（深度优先搜索）

# 题目中的“路径”中的任意节点只能出现一次。
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = None
        def search(root):
            if root is None:
                return 0
            leftMax = search(root.left)
            rightMax = search(root.right)
            self.ans = max(max(leftMax, 0) + max(rightMax, 0) + root.val, self.ans)
            return max(leftMax, rightMax, 0) + root.val
        search(root)
        return self.ans