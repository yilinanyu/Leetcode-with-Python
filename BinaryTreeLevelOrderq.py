def levelOrder(root):
	# time O(N)
	# space O(N)
	# queue and bfs to lever order.
	if not root:
		return []
	res  = []
	queue = []
	queue.append(root)

	while queue:
		size = len(queue)
		level = []
		for i in range(size):
			# pop the first element since it is a queue
			node = queue.pop(0)
			level.append(node.val)

			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
		res.append(level)
	return res

def levelOrder2(root):
	# time: O(N)
	# space: O(N)
	if not root:
		return []
	res  = []
	queue = []
	queue.append(root)
	while queue:
		size = len(queue)
		level = []

		for i in range(size):
			node = queue.pop(0)
			level.append(node.val)
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.right(node.right)
		res.insert(0, level)
	return res
