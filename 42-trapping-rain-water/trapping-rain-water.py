class Solution:
    def trap(self, height: List[int]) -> int:
        # To know water at each height need:
        # Heighest height on left, and heighest height on right at position i
        # max(0, min(maxLeft, maxRight) - height[i])

        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n

        left = 0
        right = 0
        for i in range(n):
            maxLeft[i] = left
            maxRight[n-1 - i] = right

            left = max(left, height[i])
            right = max(right, height[n-1 - i])

        trapWater = 0
        for i, h in enumerate(height):
            trapWater += max(0, min(maxLeft[i], maxRight[i]) - h)
        
        return trapWater
        