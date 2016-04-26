def binarytree(node):
	if node is None:
		return 
	return node.val + self.binarytree(node.left) + self.binarytree(node.right)