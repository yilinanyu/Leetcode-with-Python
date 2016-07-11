def validTree(self, n, edges):
	if n != len(edges) + 1:
		return False
	neighbors = {i : for i in range(n)}

	for w, v in edges:
		neighbors[w].append(v)
		neighbors[v].append(w)
	queue = [0]
	while queue:
		queue.extend(neighbors.pop(queue.pop(0),[]))
	if len(neighbors) == 0:
		return True
