class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        i = 0; j = len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target: return True
            elif matrix[i][j] > target: j -= 1
            else: i += 1
        return False