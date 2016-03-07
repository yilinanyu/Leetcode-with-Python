class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        neighbors = collections.defaultdict(set)
        for v,w in edges:
            neighbors[v].add(w)
            neighbors[w].add(v)
            
        visited = [False] *n
        res = 0
        for i in range(n):
            if visited[i] == False:
                res += 1
                queue = [i]
                visited[i] = True
                
                while queue:
                    cur = queue.pop(0)
                    for k in neighbors[cur]:
                        if visited[k] == False:
                            queue.append(k)
                            visited[k] = True
        return res
        