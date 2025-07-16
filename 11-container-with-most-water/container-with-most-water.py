class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxContainer = 0
        
        left = 0
        right = len(height) - 1

        while left < right:
            container = min(height[left], height[right]) * (right - left)
            maxContainer = max(maxContainer, container)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxContainer