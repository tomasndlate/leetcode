class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zero = 0
        for i in range(n):
            if nums[i] == 0: continue

            while zero < i and nums[zero] != 0:
                zero += 1
            
            nums[i], nums[zero] = nums[zero], nums[i]
        
        return nums