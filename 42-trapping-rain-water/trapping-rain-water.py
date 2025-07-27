class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = 0
        maxRight = 0

        trapWater = 0

        left = 0
        right = len(height) - 1

        while left <= right:
            # update minimum height
            if maxLeft <= maxRight: 
                # update left and get trap water
                trapWater += max(0, maxLeft - height[left])
                maxLeft = max(maxLeft, height[left])
                left += 1
            else: 
                # update right and get trap water
                trapWater += max(0, maxRight - height[right])
                maxRight = max(maxRight, height[right])
                right -= 1
        
        return trapWater