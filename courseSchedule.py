class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites:: List[List[int]]
        :rtype: bool
        """
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] *numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        # pick a zero indegree elment    
        zero = []
        for i in range(numCourses):
            if indegree[i] == 0:
                zero.append(i)
                
        while zero:
            cur = zero.pop(0)
            if cur in graph:
                temp = graph[cur]
                del graph[cur]
            for n in temp:
                indegree[n] -= 1
                if indegree[n] == 0:
                    zero.append(n)
        return len(graph) == 0 and sum(indegree) == 0
                
