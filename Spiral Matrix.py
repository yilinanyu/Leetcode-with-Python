class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if matrix == []: return []
        res = []
        maxUp = maxLeft = 0
        maxDown = len(matrix) - 1
        maxRight = len(matrix[0]) - 1
        direct = 0 # 0 go right, 1 go down, 2 go left, 3 go up
        while True:
            if direct == 0: # go right
                for i in xrange(maxLeft, maxRight + 1): res.append(matrix[maxUp][i])
                maxUp += 1
            elif direct == 1: 
            # go down
                for i in xrange(maxUp, maxDown + 1): res.append(matrix[i][maxRight])
                maxRight -= 1
            elif direct == 2: # go left
                for i in reversed(xrange(maxLeft, maxRight + 1)): res.append(matrix[maxDown][i])
                maxDown -= 1
            else: # go up
                for i in reversed(xrange(maxUp, maxDown + 1)): res.append(matrix[i][maxLeft])
                maxLeft += 1
            if maxUp > maxDown or maxLeft > maxRight: return res
            direct = (direct + 1) % 4