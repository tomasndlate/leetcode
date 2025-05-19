class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowi, rowj = 0, len(matrix) - 1

        while rowi <= rowj:

            rowmid = (rowj + rowi) // 2

            if matrix[rowmid][0] > target:
                rowj = rowmid - 1 # go previous mid row

            elif matrix[rowmid][-1] < target:
                rowi = rowmid + 1 # go next mid row

            else: # in this row
                i, j = 0, len(matrix[rowmid]) - 1
                while i <= j:
                    mid = (i + j) // 2
                    if matrix[rowmid][mid] > target: # reduce mid
                        j = mid - 1
                    elif matrix[rowmid][mid] < target: # increase mid
                        i = mid + 1
                    else: 
                        return True
                return False

        return False