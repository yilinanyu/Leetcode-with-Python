class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1,1]
        list = [[] for i in range(rowIndex+1)]
        list[0] = [1]
        list[1] = [1,1]
        for i in range(2, rowIndex+1):
            list[i] = [1 for j in range(i+1)]
            for j in range(1,i):
                list[i][j] = list[i-1][j-1]+list[i-1][j]
        return list[rowIndex]
        