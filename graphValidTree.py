class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n - 1:
            return False
        neighbors = { i : [] for i in range(n) }
        for v, e in edges:
            neighbors[v].append(e)
            neighbors[e].append(v)
        queue = [0]
        while queue:
            queue.extend(neighbors.pop(queue.pop(0),[]))
        return not neighbors
        
        