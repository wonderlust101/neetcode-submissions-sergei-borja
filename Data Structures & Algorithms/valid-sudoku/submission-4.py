class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_hash = defaultdict(list)
        row_hash = defaultdict(list)
        squ_hash = defaultdict(list)

        for row in range(9):
            for col in range(9):
                val = board[row][col]

                if val == '.':
                    continue

                squ = (row //3, col // 3)

                if val in col_hash[col] or val in row_hash[row] or val in squ_hash[squ]:
                    return False
                
                col_hash[col].append(val)
                row_hash[row].append(val)
                squ_hash[squ].append(val)
        
        return True