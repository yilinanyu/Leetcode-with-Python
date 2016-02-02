class Solution:
	def isBalanced(self, root):
		if root is None:
			return True
		elif abs(self.height(root.left)- self.height(root.right)) <= 1:
			return self.isBalanced(root.left) and self.isBalanced(root.right)
		else:
			return False
	def height(self, root):
		if root is None:
			return 0
		else:
			return max(self.height(root.left),self.height(root.right))+1