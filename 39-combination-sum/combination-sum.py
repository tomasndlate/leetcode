class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # BACKTRACKING
        res = []

        def dfs(start, path, total):
            if total > target:
                return
            if total == target:
                res.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(i, path, total + candidates[i])
                path.pop()
        
        dfs(0, [], 0)
        return res