class Solution:
    def maxArea(self, height: List[int]) -> int:
        # TWO POINTERS
        left = 0
        right = len(height) - 1
        
        max_area = 0
        while left < right:
            # area = width * height
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)

            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        
        return max_area


