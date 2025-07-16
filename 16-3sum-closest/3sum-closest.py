class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestSum = float('inf')
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: # skip duplicates
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                threeSum = nums[i] + nums[j] + nums[k]

                if abs(target - threeSum) < abs(target - closestSum):
                    closestSum = threeSum

                if threeSum < target:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

                elif threeSum > target:
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1

                else: # exact sum
                    return closestSum

        return closestSum