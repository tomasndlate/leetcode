class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []

        prevEnd = float('-inf')

        for start, end in intervals:
            if start <= prevEnd:
                res[-1][1] = max(prevEnd, end)
            else:
                res.append([start, end])
            prevEnd = max(prevEnd, end)
        
        return res