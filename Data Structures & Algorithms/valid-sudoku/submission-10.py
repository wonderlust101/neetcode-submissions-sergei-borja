class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHash = defaultdict(list)
        colHash = defaultdict(list)
        squHash = defaultdict(list)

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue

                if value in rowHash[r] or value in colHash[c] or value in squHash[(r//3, c//3)]:
                    return False
                
                rowHash[r].append(value)
                colHash[c].append(value)
                squHash[(r//3, c//3)].append(value)
        
        return True