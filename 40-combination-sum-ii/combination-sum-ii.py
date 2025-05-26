class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start: int, path: List[int], total: int):
            if total == target: res.append(path[:]); return
            if total > target: return

            i = start
            while i < len(candidates):
                path.append(candidates[i])
                backtrack(i+1, path, total + candidates[i])
                path.pop()
                i += 1
                while i < len(candidates) and candidates[i-1] == candidates[i]: i += 1

        backtrack(0, [], 0)
        return res