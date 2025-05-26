class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(start, path):
            res.append(path[:])
            if start >= len(nums): return

            for i in range(start, len(nums)):
                if i > start and nums[i-1] == nums[i]: continue

                path.append(nums[i])
                dfs(i+1, path[:])
                path.pop()
            
        dfs(0, [])
        return res
