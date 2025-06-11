class Solution:
    def numDecodings(self, s: str) -> int:
        # TOP-DOWN: RECURSION + MEMOIZATION
        cache = {}

        def dfs(i, j):
            if (i,j) in cache:
                return cache[(i,j)]

            # Over length of string
            if j >= len(s):
                return 0
            
            num = s[i:j+1]
            # minumum # maximum # first digit 0
            if int(num) < 1 or int(num) > 26 or num != str(int(num)):
                #cache[(i,j)] = 0
                return 0 #cache[(i,j)]

            # Reach final digit
            if j == len(s) - 1:
                #cache[(i,j)] = 1
                return 1
            
            cache[(i,j)] = dfs(j+1, j+1) + dfs(j+1, j+2)
                
            return cache[(i,j)]
        
        return dfs(0, 0) + dfs(0, 1)