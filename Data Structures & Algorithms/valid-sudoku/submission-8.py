class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = defaultdict(list)
        col_hash = defaultdict(list)
        squ_hash = defaultdict(list)

        for row in range(9):
            for col in range(9):
                # get board value
                val = board[row][col]

                # skip .
                if val == '.':
                    continue

                # get square vale
                squ = (row//3, col//3)

                # check if val in hashes
                if val in row_hash[row] or val in col_hash[col] or val in squ_hash[squ]:
                    return False

                # app to hashes                
                row_hash[row].append(val)
                col_hash[col].append(val)
                squ_hash[squ].append(val)


        return True