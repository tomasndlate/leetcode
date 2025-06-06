class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # ARRAYS AND SETS
        uniqueNums = set(nums)
        max_seq = 0

        for n in uniqueNums:
            if n - 1 in uniqueNums: # not first of sequence
                continue
            seq = n
            count = 0
            while seq in uniqueNums:
                count += 1
                max_seq = max(max_seq, count)
                seq += 1
        
        return max_seq