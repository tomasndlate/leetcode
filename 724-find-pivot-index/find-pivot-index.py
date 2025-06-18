class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        numsSum = sum(nums)
        prefixSum = 0

        for i, num in enumerate(nums):
            if prefixSum == numsSum - prefixSum - num:
                return i
            prefixSum += num
        
        return -1