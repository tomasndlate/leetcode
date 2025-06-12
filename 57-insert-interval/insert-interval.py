class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = 0, 1
        res = []

        for i, interval in enumerate(intervals):
            # before interval    
            if newInterval[end] < interval[start]:
                res.append(newInterval)
                return res + intervals[i:]
            # new goes after
            elif newInterval[start] > interval[end]:
                res.append(interval)
            # overlap
            else:
                newInterval = [min(newInterval[start], interval[start]), max(newInterval[end], interval[end])]
        
        res.append(newInterval)
        return res