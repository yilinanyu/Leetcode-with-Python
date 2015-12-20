class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        def isValid(x, y, tmp):
            for i in range(9):
                if board[i][y]==tmp:return False
            for i in range(9):
                if board[x][i]==tmp:return False
            for i in range(3):
                for j in range(3):
                    if board[(x/3)*3+i][(y/3)*3+j]==tmp: return False
            return True
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':continue
                tmp=board[i][j]
                board[i][j]='D'
                if isValid(i,j,tmp)==False: return False
                else:
                    board[i][j]=tmp
        return True