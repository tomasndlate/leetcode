class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        start, end = 0, 1
        intervals.sort(key=lambda x: x[start])

        res = [intervals[0]]
        for interval in intervals[1:]:
            if interval[start] <= res[-1][end]: # overlap
                res[-1][end] = max(res[-1][end], interval[end])
            else:
                res.append(interval)

        return res