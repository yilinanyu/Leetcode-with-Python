# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#递归， 先序遍历解决

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def NLR(node):
            if node:
                vals.append(str(node.val))
                NLR(node.left)
                NLR(node.right)
            else:
                vals.append("#")
        vals = []
        NLR(root)
        return ' '.join(vals)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # 怎样构造树呢？看看
        def NLR():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = NLR()
            node.right = NLR()
            return node
        vals = iter(data.split())
        return NLR()
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))