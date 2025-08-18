class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2
        partitions = set()
        partitions.add(0)

        for num in nums:
            newPartitions = set()
            for part in partitions:
                newPartitions.add(part + num)
            partitions.update(newPartitions)
            if target in partitions:
                return True
        
        return False