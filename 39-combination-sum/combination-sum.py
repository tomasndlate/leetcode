class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, pathSum):
            if pathSum == target:
                res.append(path[:])
                return
            if pathSum > target:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, pathSum + candidates[i])
                path.pop()
        
        backtrack(0, [], 0)
        return res