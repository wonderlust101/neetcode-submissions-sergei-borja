class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def explore(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != "O":
                return
            
            board[row][col] = "S"

            explore(row + 1, col)
            explore(row - 1, col)
            explore(row, col + 1)
            explore(row, col - 1)

        for row in range(rows):
            for col in range(cols):
                if (row in (0, rows - 1) or col in (0, cols - 1)) and board[row][col] == "O":
                    explore(row, col)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "S":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"