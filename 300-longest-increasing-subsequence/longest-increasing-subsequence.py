from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # bisect left - index where you can introduce num to keep increase order
        lis = []

        for  num in nums:
            i = bisect_left(lis, num)
            if i == len(lis):
                lis.append(num)
            else: # replace num with lower num
                lis[i] = num

        return len(lis)