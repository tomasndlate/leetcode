class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            
            if target < nums[mid]:
                if not nums[l] > nums[mid] and nums[l] > target:
                    l = mid + 1
                else:
                    r = mid - 1

            elif target > nums[mid]:
                if not nums[r] < nums[mid] and nums[r] < target:
                    r = mid - 1
                else:
                    l = mid + 1

            else: return mid

        return -1