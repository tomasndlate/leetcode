class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        # Rotate 90 steps:
        # Mirror matrix centered in vertical middle
        for r in range(rows):
            left, right = 0, cols - 1
            while left < right:
                matrix[r][left], matrix[r][right] = matrix[r][right], matrix[r][left]
                left += 1
                right -= 1

        # Mirror matrix centered in positive diagonal
        for r in range(rows):
            for c in range(cols - r):
                inverseR, inverseC = rows-1 - c, cols-1 - r
                matrix[r][c], matrix[inverseR][inverseC] = matrix[inverseR][inverseC], matrix[r][c]