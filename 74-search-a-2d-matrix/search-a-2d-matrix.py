class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_min = 0
        row_max = len(matrix) - 1
        col_min = 0
        col_max = len(matrix[0]) - 1

        while row_min <= row_max:
            row_mid = (row_min + row_max) // 2
            
            if target < matrix[row_mid][col_min]:
                row_max = row_mid - 1

            elif target > matrix[row_mid][col_max]:
                row_min = row_mid + 1
                
            else:
                while col_min <= col_max:
                    col_mid = (col_min + col_max) // 2
                    
                    if target < matrix[row_mid][col_mid]:
                        col_max = col_mid - 1

                    elif target > matrix[row_mid][col_mid]:
                        col_min = col_mid + 1

                    else:
                        return True
        
        return False
            