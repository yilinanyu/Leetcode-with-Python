class BinaryNode():
	def __init__(self, item, parent = None, left = None, right = None):
		self.item = item
		self.left = left 
		self.right = right 
		self.parent = parent

def lca_with_parent(node1, node2):
	path1 = path_from_root(node1)
	path2 = path_from_root(node2)
	lca = None
	for n1, n2 in zip(path1, path2):
		if n1 != n2:
			return lca
		lca = n1
	return lca
def path_from_root(node):
	path = []
	while node:
		path.insert(0, node)
		node = node.parent
	return path

def lca_without_parent(root, node1, node2):
	if not root:
		return None
	if root == node1 or root == node2:
		return root
	lca_in_left = lca_without_parent(root.left, node1, node2)
	lca_in_right = lca_without_parent(root.right, node1, node2)
	if lca_in_right and lca_in_left:
		return root
	return lca_in_left or lca_in_right