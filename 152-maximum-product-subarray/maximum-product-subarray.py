class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxProd = float('-inf')
        leftProd = 1
        rightProd = 1

        for i in range(n):
            leftNum = nums[i]
            rightNum = nums[n-1 - i]

            leftProd *= leftNum
            rightProd *= rightNum
            maxProd = max(maxProd, leftProd, rightProd)

            if leftProd == 0: leftProd = 1
            if rightProd == 0: rightProd = 1
        
        return maxProd