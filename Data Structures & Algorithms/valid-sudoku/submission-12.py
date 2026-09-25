class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHash = defaultdict(list)
        colHash = defaultdict(list)
        squHash = defaultdict(list)

        for row in range(9):
            for col in range(9):
                val = board[row][col]

                if val == ".":
                    continue

                squ = (row // 3, col // 3)

                if val in rowHash[row] or val in colHash[col] or val in squHash[squ]:
                    return False
                
                rowHash[row].append(val)
                colHash[col].append(val)
                squHash[squ].append(val)
        
        return True