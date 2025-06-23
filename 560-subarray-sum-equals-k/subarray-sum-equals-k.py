class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumCount = defaultdict(int)
        prefixSumCount[0] = 1
        prefixSum = 0
        count = 0

        for num in nums:
            prefixSum += num
            prefix = prefixSum - k
            
            count += prefixSumCount[prefix]
            prefixSumCount[prefixSum] += 1
        
        return count