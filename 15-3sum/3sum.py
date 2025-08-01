class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: # avoid repeated numbers
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k:
                threeSum = nums[i] + nums[j] + nums[k]

                if threeSum < 0:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

                elif threeSum > 0:
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k-= 1
                        
                else: # threeSum equals zero
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k-= 1
                        
        return res
