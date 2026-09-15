class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowsSeen = defaultdict(list)
        columnsSeen = defaultdict(list)
        squaresSeen = defaultdict(list)

        for row in range(9):
            for column in range(9):
                val = board[row][column]

                if val == ".":
                    continue
                
                if val in rowsSeen[row] or val in columnsSeen[column] or val in squaresSeen[(row//3, column//3)]:
                    return False
                
                rowsSeen[row].append(val)
                columnsSeen[column].append(val)
                squaresSeen[(row//3, column//3)].append(val)
        
        return True