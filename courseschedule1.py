class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        zeroInDegree = set()
        degree = [0] * numCourses
        
        for pre in prerequisites:
            degree[pre[0]] += 1
        
        for i in range(len(degree)):
            if degree[i] == 0:
                zeroInDegree.add(i)
            
        if not zeroInDegree:
            return False
        
        while zeroInDegree:
            it = iter(zeroInDegree)
            course = it.next()
            zeroInDegree.remove(course)
            
            for i in range(len(prerequisites)):
                edge = prerequisites[i]
                if edge[1] == course:
                    degree[edge[0]] -= 1
                    if degree[edge[0]] == 0:
                        zeroInDegree.add(edge[0])
        
        return sum(degree) == 0