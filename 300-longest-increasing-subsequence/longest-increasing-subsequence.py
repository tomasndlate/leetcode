class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        lis = 1

        for cur in range(n):
            for prev in range(cur):
                if nums[cur] > nums[prev]:
                    dp[cur] = max(dp[cur], 1 + dp[prev])
                    lis = max(lis, dp[cur])

        return lis