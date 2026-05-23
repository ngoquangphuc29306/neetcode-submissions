class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Subproblem 1 : Validate Row
        for row in range(0, 9):
            seen = set()
            for i in range(0, 9):
                x = board[row][i]
                if x in seen:
                    return False
                elif x != '.':
                    seen.add(x)
        #Subproblem 2 : Validate Col
        for col in range(0, 9):
            seen = set()
            for i in range(0, 9):
                x = board[i][col]
                if x in seen:
                    return False
                elif x != '.':
                    seen.add(x)
        #Sub problem 3 : Validate sub_box
        starts = [
            (0, 0), (0, 3), (0, 6),
            (3, 0), (3, 3), (3, 6),
            (6, 0), (6, 3), (6, 6)
        ]
        for init_r, init_c in starts:
            seen = set()
            for row in range(init_r, init_r + 3):
                for col in range(init_c, init_c + 3):
                    x = board[row][col]
                    if x in seen:
                        return False
                    elif x != '.':
                        seen.add(x)
        return True
