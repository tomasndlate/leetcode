class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        max_count = 0
        for num in uniqueNums:
            # begin of sequence
            if num - 1 in uniqueNums: continue
            
            count = 0
            n = num
            while n in uniqueNums:
                count += 1
                n += 1
            
            max_count = max(max_count, count)
        
        return max_count