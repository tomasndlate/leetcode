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
                seq += 1
            max_seq = max(max_seq, count)
        
        return max_seq