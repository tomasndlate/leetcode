class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0

        for row in range(n):
            for col in range(n):
                i = 0
                while i < n and grid[row][i] == grid[i][col]:
                    i += 1
                
                if i == n: # equal row and col 
                    count += 1
        
        return count