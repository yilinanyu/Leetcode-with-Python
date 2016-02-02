class Codec:
	def serialize(self, node):
		# pre order
		def NLR(node):
			if node:
				vals.append(str(node.val))
				NLR(node.left)
				NLR(node.right)
			else:
				vals.append("#")
		vals = []
		NLR(root)
		return ''.join(vals)
	def  deserialize(self, data):
		# make a tree
		def NLR():
			val = next(vals)
			if val == "#":
				return None
			node = TreeNode(int(val))
			node.left = NLR()
			node.right = NLR()
			return node
		vals = iter(data.split())
		return NLR()


