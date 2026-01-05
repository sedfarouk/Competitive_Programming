class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)

        intervals.sort()
        res = []
        i = 0

        while i < n:
            st, end = intervals[i]
            while i < n and end >= intervals[i][0]:
                end = max(end, intervals[i][1])
                i += 1
            res.append([st, end])

        return res
