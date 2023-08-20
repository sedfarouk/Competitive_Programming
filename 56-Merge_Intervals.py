# 56. Leetcode - Merge Intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key=lambda x:x[0])
        max_val = intervals[0][1]
        min_val = intervals[0][0]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= max_val:
                max_val = max(max_val, intervals[i][1])
            else:
                ans.append([min_val, max_val])
                min_val = intervals[i][0]
                max_val = intervals[i][1]

        ans.append([min_val, max_val])

        return ans

        
