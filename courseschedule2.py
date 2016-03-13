class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):
        res = []
        zeroInDegree = set()
        degree = [0] * numCourses
        
        for course, pre in prerequisites:
            degree[course] += 1
        
        for i in range(len(degree)):
            if degree[i] == 0:
                zeroInDegree.add(i)
        
        if not zeroInDegree:
            return []
        
        queue = list(zeroInDegree)
        while queue:
            course = queue.pop(0)
            res.append(course)
            
            for cur, pre in prerequisites:
                if pre == course:
                    degree[cur] -= 1
                    if degree[cur] == 0:
                        queue.append(cur)
                        
        if sum(degree) == 0:
            return res
        return []