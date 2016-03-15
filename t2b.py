# // # Let's assume the input ternary expression is valid, we can build the tree in preorder manner.

# // # Each time we scan two characters, the first character is either ? question mark or : colon,
# // # the second character holds the value of the tree node. When we see ?, 
# // #we add the new node to left. 
# // #When we see :, we need to find out the ancestor node that doesn't have a right node, and make the new node as its right child.

def covertToBST(expression):
	root = TreeNode(expression[0])
	stack = []
	for i in range(0, len(expression),2):
		if expression[i] == "?":
			root.left = TreeNode(expression[i+1])
			stack.append(root)
			root = root.left
		elif expression[i] == ":":
			root = stack.pop()
			while root.right != None:
				root = stack.pop()
			root.right = TreeNode(expression[i+1])
			root = root.right
	return root