class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixCount = collections.defaultdict(int)
        prefixCount[0] = 1
        
        prefixSum = 0
        count = 0
        for n in nums:
            prefixSum += n
            complement = prefixSum - k # complement + k = prefix 
            count += prefixCount[complement]
            prefixCount[prefixSum] += 1
        
        return count