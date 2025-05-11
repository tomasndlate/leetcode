class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_nums = set(nums)
        max_seq = 0
        for n in hash_nums:
            if n-1 not in hash_nums: # seq beginning
                count = 0
                start = n
                while start in hash_nums:
                    count += 1
                    start += 1
                max_seq = max(max_seq, count)
        
        return max_seq
        