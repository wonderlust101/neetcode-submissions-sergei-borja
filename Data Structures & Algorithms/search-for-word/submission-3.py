class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def explore(r, c, i):
            if len(word) == i:
                return True
            
            if r >= rows or r < 0 or c >= cols or c < 0:
                return False
            
            if board[r][c] != word[i]:
                return False
            
            board[r][c] = '#'

            result = (explore(r + 1, c, i + 1) or
                        explore(r, c + 1, i + 1) or
                        explore(r - 1, c, i + 1) or
                        explore(r, c - 1, i + 1))

            board[r][c] = word[i]
            
            return result

        for r in range(rows):
            for c in range(cols):
                if explore(r, c, 0):
                    return True
        
        return False