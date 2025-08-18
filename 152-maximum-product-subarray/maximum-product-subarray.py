class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        
        n = len(nums)
        leftProd = rightProd = 1
        maxProd = nums[0]

        for i in range(n):
            leftProd *= nums[i]
            rightProd *= nums[n-1 - i]

            maxProd = max(maxProd, leftProd, rightProd)
            
            if leftProd == 0: leftProd = 1
            if rightProd == 0: rightProd = 1
        
        return maxProd