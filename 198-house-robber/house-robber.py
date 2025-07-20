class Solution:
    def rob(self, nums: List[int]) -> int:
        
        house1, house2 = 0, 0
        for num in nums:
            house1, house2 = house2, max(house1 + num, house2)
        
        return max(house1, house2)