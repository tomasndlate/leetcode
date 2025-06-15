class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # left sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target and target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
                    
            # right sorted
            else:
                if nums[mid] <= target and target <= nums[right]:
                    left = mid
                else:
                    right = mid - 1
        
        return -1