class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        for i in xrange(n / 2):
            for j in xrange(n):
                matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]
        for i in xrange(n):
            for j in xrange(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
