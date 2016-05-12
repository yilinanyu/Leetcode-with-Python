class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        if numRows > 2:
            list = [[] for i in range(numRows)]
            for i in range(0, numRows):
                list[i] = [1 for j in range(i + 1)]
            for i in range(2, numRows):
                for j in range(1, i):
                    list[i][j] = list[i - 1][j - 1] + list[i - 1][j]
            return list