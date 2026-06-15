class Solution:
    def solveNQueens(self, n: int):
        res = []

        cols = set()
        diag1 = set()   # row - col
        diag2 = set()   # row + col

        board = ['.' * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                res.append(board[:])
                return

            for col in range(n):

                if (col in cols or
                    row - col in diag1 or
                    row + col in diag2):
                    continue

                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                board[row] = (
                    board[row][:col]
                    + 'Q'
                    + board[row][col + 1:]
                )

                backtrack(row + 1)

                board[row] = (
                    board[row][:col]
                    + '.'
                    + board[row][col + 1:]
                )

                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)

        return res