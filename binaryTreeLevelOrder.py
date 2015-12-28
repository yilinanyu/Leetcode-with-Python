class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res, queue = [], collections.deque([root])
        while queue:
            level = []
            for i in xrange(len(queue)):
                x = queue.popleft()
                level.append(x.val)
                if x.left: queue.append(x.left)
                if x.right: queue.append(x.right)
            res.append(level)
        return res