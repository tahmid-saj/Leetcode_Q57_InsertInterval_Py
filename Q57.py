class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = j = bisect_left(intervals, [newInterval[1]+1]) - 1
        while i >= 0 and intervals[i][1] >= newInterval[0]:
            newInterval = sorted(newInterval + intervals[i])[::3]
            i -= 1
        intervals[i+1:j+1] = [newInterval]
        return intervals
