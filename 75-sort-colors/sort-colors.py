class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_i = 0
        two_i = len(nums) - 1

        i = 0
        while i <= two_i:

            if nums[i] == 0:
                nums[i], nums[zero_i] = nums[zero_i], nums[i]
                zero_i += 1
                i += 1

            elif nums[i] == 1:
                i += 1

            elif nums[i] == 2:
                nums[i], nums[two_i] = nums[two_i], nums[i]
                two_i -= 1