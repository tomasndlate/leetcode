class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1

        n = len(nums)
        prefixSum = [0] * (n + 1)
        #prefixSum[0] = nums[0]

        for i in range(n):
            prefixSum[i+1] = prefixSum[i] + nums[i]
        
        print(prefixSum)

        for i in range(n):
            if prefixSum[i] == prefixSum[-1] - prefixSum[i+1]:
                return i
        
        return -1
