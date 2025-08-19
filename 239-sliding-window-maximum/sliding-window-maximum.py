from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = deque()

        for i in range(len(nums)):
            # pop lower nums indexes from window, and add
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            window.append(i)

            # popleft index no longer in window
            if window and i - window[0] >= k:
                window.popleft()

            # if window fixed, append the current max (most left num)
            if i + 1 >= k:
                res.append(nums[window[0]])
        
        return res
        