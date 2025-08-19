class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return
            
            for i in range(start, len(candidates)):
                if i > 0 and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])
                path.pop()
        
        backtrack(0, [], 0)
        return res