class Solution:
    def numDecodings(self, s: str) -> int:
        # TOP-DOWN: RECURSION + MEMOIZATION
        n = len(s)
        cache = {}

        def dfs(i):
            if i in cache: return cache[i]

            # reach final
            if i >= n: return 1

            if s[i] == '0': return 0

            # 1 DIGIT (valid)
            res = dfs(i+1) # send 1 digit after

            # 2 DIGIT (check if valid)
            if i + 1 < n and 1 <= int(s[i:i+2]) and int(s[i:i+2]) <= 26:
                res += dfs(i+2) # send 2 digit after

            cache[i] = res
            return cache[i]
        
        return dfs(0)