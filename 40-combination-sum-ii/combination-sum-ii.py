class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        candidates.sort()

        def dfs(start, path, total):
            if total == target: res.append(path); return
            if total > target or start >= n: return
            
            for i in range(start, n):
                if i > start and candidates[i-1] == candidates[i]:
                    continue
                path.append(candidates[i])
                dfs(i+1, path[:], total + candidates[i])
                path.pop()
        
        dfs(0, [], 0)
        
        return res
        