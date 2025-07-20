class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0: return 0
        if n == 1: return nums[0]

        def helper(houses):
            house1, house2 = 0, 0
            for house in houses:
                house1, house2 = house2, max(house1 + house, house2)
            
            return max(house1, house2)

        return max(helper(nums[1:]), helper(nums[:n-1]))