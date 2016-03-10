class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        q = []

        node = root
        q.append([node,0])

        output = {}

        while len(q) > 0:
            node,level = q.pop(0)

            if not (level in output):
                output[level] = [node.val]
            else:
                output[level].append(node.val)

            if node.left is not None:
                q.append([node.left,level-1])
            if node.right is not None:
                q.append([node.right,level+1])

        sortedkeys = sorted(output.keys())
        vertorder = []
        for i in sortedkeys:
            vertorder.append(output[i])
        return vertorder