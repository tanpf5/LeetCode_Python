__author__ = 'Vigery'

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    a = board[i][j]
                    for k in range(9):
                        if board[i][k] == a and k != j:
                            return False
                        if board[k][j] == a and k != i:
                            return False
                    x, y = i // 3, j // 3
                    for m in range(3):
                        for n in range(3):
                            if board[x * 3 + m][y * 3 + n] == a and not (x * 3 + m == i and y * 3 + n == j):
                                return False
        return True

s = Solution()
