# //O(N)
 # Let's assume the input ternary expression is valid, we can build the tree in preorder manner.

# // # Each time we scan two characters, the first character is either ? question mark or : colon,
# // # the second character holds the value of the tree node. When we see ?, 
# // #we add the new node to left. 
# // #When we see :, we need to find out the ancestor node that doesn't have a right node, and make the new node as its right child.

def covertToBST(expression):
	if len(expression) == 0: return None
	root = TreeNode(expression[0])
	#save a reference to the root of the tree and return that, it might be even better
	n = root
	stack = []
	for i in range(1, len(expression),2):
		if expression[i] == "?":
			n.left = TreeNode(expression[i+1])
			stack.append(n)
			n = n.left
		elif expression[i] == ":":
			n = stack.pop()
			while n.right != None:
				n = stack.pop()
			n.right = TreeNode(expression[i+1])
			stack.append(n)
			n = n.right
	return root