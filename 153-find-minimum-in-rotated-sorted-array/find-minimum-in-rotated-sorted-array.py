class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float('inf')

        while l <= r:
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[l] > nums[mid]: # rotated on left
                r = mid - 1
            elif nums[r] < nums[mid]: # rotated on right
                l = mid + 1
            else: # all sorted
                return min(res, nums[l])
        
        return res
        