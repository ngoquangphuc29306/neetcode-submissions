class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])

        used = [[False for _ in range(m)] for _ in range(n)]

        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0 ,0]

        check = False

        def Try(i, j, pos):
            if pos == len(word):
                return True
            
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]

                if (
                    0 <= x < n and
                    0 <= y < m and
                    used[x][y] == False and
                    board[x][y] == word[pos]
                ):
                    used[x][y] = True

                    if Try(x, y, pos + 1):
                        return True
                    
                    used[x][y] = False
            
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    used[i][j] = True

                    if Try(i, j, 1):
                        return True
                    
                    used[i][j] = False

        return False