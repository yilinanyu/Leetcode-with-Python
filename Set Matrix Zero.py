class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rownum = len(matrix)
        colnum = len(matrix[0])
        row = [False for i in range(rownum)]
        colum = [False for i in range(colnum)]
        for i in range(rownum):
            for j in range(colnum):
                if matrix[i][j]==0:
                    row[i] = True
                    colum[j] = True
        for i in range(rownum):
            for j in range(colnum):
                if row[i] or colum[j]:
                    matrix[i][j]=0
                    