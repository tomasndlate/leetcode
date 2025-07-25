class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        left = 0
        right = len(nums) - 1

        while left <= right:

            while left < right and nums[left] == nums[left+1]:
                left += 1

            while left < right and nums[right] == nums[right-1]:
                right -= 1

            if left < right and nums[left] == nums[right]:
                left += 1

            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # left sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # right sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False