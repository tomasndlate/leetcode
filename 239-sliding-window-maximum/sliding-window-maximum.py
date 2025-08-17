from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = deque()
        #left = 0
        for i, num in enumerate(nums):

            # pop smaller numbers
            while window and nums[window[-1]] < num:
                window.pop()
            window.append(i)

            # remove index no longer within window
            while window and i - window[0] + 1 > k:
                window.popleft()
            
            # window is in fixed size
            if i + 1 >= k:
                res.append(nums[window[0]])
        
        return res