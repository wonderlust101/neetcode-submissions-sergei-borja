class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = defaultdict(set)
        column_hash = defaultdict(set)
        square_hash = defaultdict(set)

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                
                square = (row//3, col//3)

                if val in row_hash[row] or val in column_hash[col] or val in square_hash[square]:
                    return False

                row_hash[row].add(val)
                column_hash[col].add(val)
                square_hash[square].add(val)
        
        return True