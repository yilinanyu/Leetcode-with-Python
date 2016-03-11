class Solution:
    # @param {integer} n
    # @return {integer}
    def totalNQueens(self, n):
        self.queens = 0
        self.dfs(n, [-1] * n, 0)
        return self.queens
        
    def dfs(self, n, colForRow, row):
        if row == n:
            self.queens += 1
            return
        
        for c in range(len(colForRow)):
            flag = True
            for r in range(row):
                if colForRow[r] == c or abs(colForRow[r] - c) == row - r:
                    flag = False
            if flag:
                colForRow[row] = c
                self.dfs(n, colForRow, row + 1)
