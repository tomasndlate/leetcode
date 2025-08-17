class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start):
            if start == len(nums):
                res.append(nums[:])

            duplicates = set()
            for i in range(start, len(nums)):
                if nums[i] in duplicates:
                    continue
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[i], nums[start] = nums[start], nums[i]
                duplicates.add(nums[i])
        
        backtrack(0)
        return res