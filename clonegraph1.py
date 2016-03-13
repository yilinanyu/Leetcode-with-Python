# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        
        dic = {}
        return self.dfs(node, dic)
    
    def dfs(self, node, dic):
        if node in dic:
            return dic[node]
        
        newNode = UndirectedGraphNode(node.label)
        dic[node] = newNode
        
        for n in node.neighbors:
            newNode.neighbors.append(self.dfs(n, dic))
        
        return newNode