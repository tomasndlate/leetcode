class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        maxSeq = 1

        for i in range(n):
            for j in range(i-1, -1, -1): # what is backwards
                if nums[i] > nums[j]: # increasing
                    dp[i] = max(dp[i], 1 + dp[j])
                    maxSeq = max(maxSeq, dp[i])
        
        print(dp)
        return maxSeq
        