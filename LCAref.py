#明确题意： one node is the ancester of one node
# wheather have a parent node in my tree implementation
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# class BinaryNode():
# #The method O(n) time, but requires three tree traversals plus extra spaces for path arrays. 
# 	def __init__(self, item, parent = None, left = None, right = None):
# 		self.item = item
# 		self.left = left 
# 		self.right = right 
# 		self.parent = parent
# def lca_of_binarySearchTree(root, node1, node2):
# 	if not root:
# 		return None
# 	if root == node1 or root == node2:
# 		return root
# 	elif root.val > node1.val and root.val > node2.val:
# 		return lca_of_binarySearchTree(root.left, node1, node2)
# 	elif root.val < node1.val and root.val < node2.val:
# 		return lca_of_binarySearchTree(root.right, node1, node2)
# 	else:
# 		return root

# find the path from node 1 and node 2 up to the root. and find where they first diverge

def lca_with_parent(node1, node2):
	path1 = path_from_root(node1)
	path2 = path_from_root(node2)
	lca = None
	# zip: iterate through each node until the shortest end
	for n1, n2 in zip(path1, path2):
		if n1 != n2:
			return lca
		lca = n1
	return lca
def path_from_root(node):
	path = []
	# reverse order of we find the path : start from the root and ends up with the node
	while node:
		path.insert(0, node)
		# go up the tree
		node = node.parent
	return path

#he idea is to traverse the tree starting from root. 
#If any of the given keys (n1 and n2) matches with root, 
#then root is LCA (assuming that both keys are present). 
#If root doesn’t match with any of the keys, we recur for left and right subtree. 
#The node which has one key present in its left subtree and the other key present in right subtree is the LCA. 
#If both keys lie in left subtree, then left subtree has LCA also, otherwise LCA lies in right subtree.
# O(N)

def lca_without_parent(root, node1, node2):
        # if we can not find this node or node is None return none
        if not root:
            return None
        # if my node equals to p or q, we return root, means we find it 
        if root == p or root == q:
            return root
        # the find result in lca in left is the way we find in the left root of the root
        # same as right.
        # if we find one, return the root, if not return none
        lca_in_left = self.lca_without_parent(root.left, p, q)
        lca_in_right = self.lca_without_parent(root.right, p, q)
        # if right and left both find, which means, one node is in left site and other one is in right site, in this case, return lca is the root
        if lca_in_right and lca_in_left:
            return root
        # otherwise, we found at left and return node at right site, which mean two nodes are at the same sites. in this case, return the l
        return lca_in_left or lca_in_right