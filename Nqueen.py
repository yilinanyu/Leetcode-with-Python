class Solution:
    # @param {integer} n
    # @return {string[][]}
    def solveNQueens(self, n):
        self.res = []
        self.helper(n, 0, [], [-1] * n)
        return self.res
        
    def helper(self, n, row, line, colForRow):
        if row == n:
            self.res.append(line)
            return
        
        for c in range(n):
            flag = True
            for r in range(row):
                if colForRow[r] == c or abs(colForRow[r] - c) == row - r:
                    flag = False
                    
            if flag:
                colForRow[row] = c
                s = '.' * n
                self.helper(n, row + 1, line + [s[:c] + 'Q' + s[c + 1:]], colForRow)