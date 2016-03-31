# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    # #O(n) time, O(n) space

    #We need a queue to put nodes.
    def cloneGraph(self, node):
        if not node:
            return None
        
        queue = []
        dic = {}
        
        queue.append(node)
        nodeCopy = UndirectedGraphNode(node.label)
        dic[node] = nodeCopy
        
        while queue:
            cur = queue.pop(0)
            
            for n in cur.neighbors:
                if n in dic:
                    dic[cur].neighbors.append(dic[n])
                else:
                    neighborCopy = UndirectedGraphNode(n.label)
                    dic[cur].neighbors.append(neighborCopy)
                    dic[n] = neighborCopy
                    queue.append(n)
        
        return nodeCopy