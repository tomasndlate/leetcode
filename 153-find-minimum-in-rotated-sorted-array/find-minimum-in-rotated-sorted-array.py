class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float('inf')

        while l <= r:
            if nums[l] < nums[r]: # all section sorted
                return min(res, nums[l])

            mid = (l + r) // 2
            res = min(res, nums[mid])

            if nums[l] > nums[mid]: # rotated on left
                r = mid - 1
            else: # rotated on right
                l = mid + 1
                
        
        return res
        