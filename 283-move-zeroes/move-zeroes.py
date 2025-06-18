class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        
        for i in range(len(nums)):
            if nums[i] == 0: continue

            while zero < i and nums[zero] != 0:
                zero += 1
            
            nums[i], nums[zero] = nums[zero], nums[i]
        
        return nums