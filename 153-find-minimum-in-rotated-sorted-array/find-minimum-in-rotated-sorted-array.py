class Solution:
    def findMin(self, nums: List[int]) -> int:
        # BINARY SEARCH
        if not nums: return -1

        left, right = 0, len(nums) - 1
        
        # while not sorted
        while nums[left] > nums[right]:
            mid = (left + right) // 2
            # sorted left, send to right rotate side
            if nums[left] <= nums[mid]:
                left = mid + 1
            # if sorted right, send to left rotate side
            else:
                right = mid

        return nums[left]
        