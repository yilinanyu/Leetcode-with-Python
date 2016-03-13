class UnionFind:
    def __init__(self, n):
        self.count = n
        self.father = {}
        for i in range(n):
            self.father[i] = i
    
    def compressed_find(self, x):
        parent = self.father.get(x)
        while parent != self.father.get(parent):
            parent = self.father.get(parent)
        
        temp = -1
        fa = self.father.get(x)
        while fa != self.father.get(fa):
            temp = self.father.get(fa)
            self.father[fa] = parent
            fa = temp
        
        return parent
    
    def union(self, x, y):
        fa_x = self.compressed_find(x)
        fa_y = self.compressed_find(y)
        if fa_x != fa_y:
            self.father[fa_x] = fa_y
            self.count -= 1
            return True
        else:
            return False
        
        
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        
        if edges == None:
            return False
        
        uf = UnionFind(n)
        
        for e in edges:
            flag = uf.union(e[0], e[1])
            if flag == False:
                return False
        
        return uf.count == 1