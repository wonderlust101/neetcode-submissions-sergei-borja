class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Grab the length of rows and cols
        rows, cols = len(board), len(board[0])

        # Get the current cell and the current index of the word
        def explore(r, c, i):
            # If every letter match
            if len(word) == i:
                return True
            
            # Stay within grid
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            
            # If letter don't matcch
            if word[i] != board[r][c]:
                return False
            
            # Visited cell
            board[r][c] = '#'

            found = (explore(r + 1, c, i + 1) or 
                    explore(r, c + 1, i + 1) or 
                    explore(r - 1, c, i + 1) or
                    explore(r, c - 1, i + 1))
            
            # Unmark cell
            board[r][c] = word[i]

            return found


        # Go through each cell
        for r in range(rows):
            for c in range(cols):
                # If the word is able to be formed, return True
                if explore(r, c, 0):
                    return True
        
        return False