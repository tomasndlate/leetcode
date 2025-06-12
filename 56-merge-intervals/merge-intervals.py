class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        start, end = 0, 1
        intervals.sort(key=lambda interval: interval[start])
        res = []

        for interval in intervals:
            if res and interval[start] <= res[-1][end]: # overlap
                res[-1][end] = max(res[-1][end], interval[end])
            else:
                res.append(interval)
        
        return res