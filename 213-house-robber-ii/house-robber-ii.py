class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def maxRob(houses):
            house1 = house2 = 0

            for house in houses:
                robHouse = house + house1
                skipHouse = house2

                house1, house2 = house2, max(robHouse, skipHouse)
            
            return house2
        
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]
        
        return max(maxRob(nums[1:]), maxRob(nums[:-1]))
        