class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumMap = defaultdict(int)
        sumMap[0] = 1 # total 0 happen if no subarray
        prefixSum = 0
        count = 0

        for num in nums:
            prefixSum += num
            count += sumMap[prefixSum - k]
            sumMap[prefixSum] += 1
        
        return count
