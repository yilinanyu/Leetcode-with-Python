class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)  # 行
        n = len(matrix[0])  # 列
        l = 0
        r = m * n - 1   # 一维变二维
        while l <= r:
            mid = l + (r - l) / 2
            row = mid / n   # 行
            col = mid % n  # 列
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
            
        