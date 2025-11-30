class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)

        intervals.sort()
        i = 0
        ans = []

        while i < n:
            st, end = intervals[i]

            while i < n and intervals[i][0] <= end:
                end = max(intervals[i][1], end)
                i += 1

            ans.append([st, end])

        return ans