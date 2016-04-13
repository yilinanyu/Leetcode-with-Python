class Solution(object):
#     O(n^2) time
# O(n) space
    def isValidSudoku(self, board):
        for i in range(9):
            d = set()
            for j in range(9):
                x = board[i][j]
                if x != '.':
                    if x in d:
                        return False
                    d.add(x)
        
        for j in range(9):
            d = set()
            for i in range(9):
                x = board[i][j]
                if x != '.':
                    if x in d:
                        return False
                    d.add(x)
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                d = set()
                for a in range(i, i + 3):
                    for b in range(j, j + 3):
                        x = board[a][b]
                        if x != '.':
                            if x in d:
                                return False
                            d.add(x)
        
        return True
        