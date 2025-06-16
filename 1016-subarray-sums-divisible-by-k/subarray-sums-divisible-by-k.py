from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        modMap = defaultdict(int)
        modMap[0] = 1
        prefixSum = 0
        count = 0

        for num in nums:
            prefixSum += num
            count += modMap[prefixSum % k]
            modMap[prefixSum % k] += 1

        return count
