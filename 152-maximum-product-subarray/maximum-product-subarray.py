class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxProd = float('-inf')
        minProd = float('inf')

        leftProd = 1
        rightProd = 1
        for i in range(n):
            leftNum = nums[i]
            rightNum = nums[n-1 - i]

            leftProd *= leftNum
            rightProd *= rightNum

            maxProd = max(maxProd, leftProd, rightProd)
            minProd = min(minProd, leftProd, rightProd)

            leftProd = leftProd if leftProd else 1
            rightProd = rightProd if rightProd else 1
        
        return maxProd