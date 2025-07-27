class Solution:
    def rob(self, nums: List[int]) -> int:
        house1 = 0
        house2 = 0

        for house in nums:

            robHouse = house + house1
            skipHouse = house2

            house1, house2 = house2, max(robHouse, skipHouse)
        
        return house2