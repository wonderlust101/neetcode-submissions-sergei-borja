class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l, r = 0, rows * cols - 1

        while l <= r:
            m = l + ((r - l) // 2)

            row = m // cols
            col = m % cols
            
            print(row, col, m)

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = m - 1
            elif matrix[row][col] < target:
                l = m + 1
        
        return False