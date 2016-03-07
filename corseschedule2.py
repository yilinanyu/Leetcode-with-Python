class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
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
              
        res = []  
        while zero:
            node = zero.pop(0)
            res.append(node)
           
            for n in graph[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    zero.append(n)
        
        return res if sum(indegree) == 0 else []
                
