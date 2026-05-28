class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_row = len(matrix)
        n_col = len(matrix[0])

        # will do BS from low = 0 to high = n_row * n_col
        low = 0
        high = n_row * n_col - 1

        while low <= high:
            mid = (high - low) // 2 + low
            row = mid // n_col
            col = mid % n_col

            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                # decreasing the range
                high = mid - 1
            else:
                low = mid + 1
        
        return False