class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i, num in enumerate(nums):
            # target = num + complement
            complement = target - num
            if complement in complements:
                return [complements[complement], i]
            complements[num] = i