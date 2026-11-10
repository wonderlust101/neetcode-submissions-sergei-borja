class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(row, col):
            if 0 > row or row >= rows or 0 > col or col >= cols or board[row][col] != "O":
                return
            
            board[row][col] = "S"

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

            return

        for row in range(rows):
            for col in range(cols):
                if (row in (0, rows - 1) or col in (0, cols - 1)) and board[row][col] == "O":
                    dfs(row, col)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "S":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"