class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]: continue
            j, k = i + 1, n - 1
            while j < k:
                threeSum = nums[i] + nums[j] + nums[k]
                if threeSum < 0: j += 1
                if threeSum > 0: k -= 1
                if threeSum == 0: 
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k: j+= 1

        return res
        