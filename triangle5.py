class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if len(triangle) == 0: return 0
        array = [0 for i in range(len(triangle))]
        array[0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i]) - 1, -1, -1):
                if j == len(triangle[i]) - 1:
                    array[j] = array[j-1] + triangle[i][j]
                elif j == 0:
                    array[j] = array[j] + triangle[i][j]
                else:
                    array[j] = min(array[j-1], array[j]) + triangle[i][j]
        return min(array)